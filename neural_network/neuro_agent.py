from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import PromptTemplate
from typing import List, Dict, Any
import json

# === 2. Инициализация модели (бесплатная, локальная) ===
llm_pipeline = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype="auto",
    device_map="cpu",  # или "auto" если есть GPU
    max_new_tokens=300
)

llm = HuggingFacePipeline(pipeline=llm_pipeline)

# === 3. Определение инструментов ===
@tool
def get_time(location: str) -> str:
    """Получить текущее время в указанном городе."""
    return f"Текущее время в {location}: 14:00"

@tool
def calculate(operation: str) -> str:
    """Выполнить математическую операцию."""
    try:
        result = eval(operation)
        return str(result)
    except Exception as e:
        return f"Ошибка в вычислении: {e}"

# === 4. Создание промпта для ReAct агента ===
react_prompt = PromptTemplate.from_template("""
Ты полезный ассистент. Используй доступные инструменты для ответа на вопросы.

Доступные инструменты:
{tools}

История разговора:
{chat_history}

Вопрос: {input}

Отвечай в формате:
Thought: твой анализ
Action: название_инструмента
Action Input: аргументы инструмента в формате JSON
Observation: результат выполнения инструмента
Final Answer: окончательный ответ

Если инструменты не нужны, просто дай ответ:
Final Answer: твой ответ
""")

# === 5. Создание простого агента без использования create_react_agent ===
class SimpleReactAgent:
    def __init__(self, llm, tools, prompt):
        self.llm = llm
        self.tools = {tool.name: tool for tool in tools}
        self.prompt = prompt
        
    def _format_tools(self):
        tool_descriptions = []
        for name, tool in self.tools.items():
            tool_descriptions.append(f"{name}: {tool.description}")
        return "\n".join(tool_descriptions)
    
    def _parse_response(self, response_text):
        """Парсит ответ модели для извлечения действий"""
        lines = response_text.strip().split('\n')
        thought = ""
        action = None
        action_input = None
        final_answer = ""
        
        for line in lines:
            if line.startswith("Thought:"):
                thought = line[8:].strip()
            elif line.startswith("Action:"):
                action = line[7:].strip()
            elif line.startswith("Action Input:"):
                try:
                    action_input = json.loads(line[13:].strip())
                except:
                    action_input = line[13:].strip()
            elif line.startswith("Final Answer:"):
                final_answer = line[13:].strip()
                
        return {
            "thought": thought,
            "action": action,
            "action_input": action_input,
            "final_answer": final_answer
        }
    
    def invoke(self, inputs):
        messages = inputs.get("messages", [])
        chat_history = "\n".join([f"{msg.type}: {msg.content}" for msg in messages[:-1]])
        user_input = messages[-1].content if messages else ""
        
        # Формируем промпт
        prompt_text = self.prompt.format(
            tools=self._format_tools(),
            chat_history=chat_history,
            input=user_input
        )
        
        # Получаем ответ от модели
        response = self.llm.invoke(prompt_text)
        parsed = self._parse_response(response)
        
        # Если нужно выполнить действие
        if parsed["action"] and parsed["action"] in self.tools:
            tool = self.tools[parsed["action"]]
            try:
                tool_result = tool.invoke(parsed["action_input"])
                # Возвращаем результат инструмента
                return {"messages": [
                    HumanMessage(content=user_input),
                    AIMessage(content=f"Thought: {parsed['thought']}\nAction: {parsed['action']}\nAction Input: {parsed['action_input']}"),
                    ToolMessage(content=str(tool_result), tool_call_id=parsed["action"]),
                    AIMessage(content=f"Final Answer: {tool_result}")
                ]}
            except Exception as e:
                error_msg = f"Ошибка при выполнении инструмента: {str(e)}"
                return {"messages": [
                    HumanMessage(content=user_input),
                    AIMessage(content=error_msg)
                ]}
        else:
            # Простой ответ
            return {"messages": [
                HumanMessage(content=user_input),
                AIMessage(content=parsed["final_answer"] or response)
            ]}

# === 6. Создание агента ===
tools = [get_time, calculate]
agent = SimpleReactAgent(llm=llm, tools=tools, prompt=react_prompt)

# === 7. Пример запуска ===
def run_agent(query: str):
    inputs = {"messages": [HumanMessage(content=query)]}
    response = agent.invoke(inputs)
    for msg in response["messages"]:
        if isinstance(msg, HumanMessage):
            print("[Пользователь]:", msg.content)
        elif isinstance(msg, AIMessage):
            print("[Ассистент]:", msg.content)
        elif isinstance(msg, ToolMessage):
            print("[Инструмент]:", msg.content)

# === 8. Запуск ===
if __name__ == "__main__":
    run_agent("Когда выйдет iPhone 17?")
    print("\n" + "="*50 + "\n")
    run_agent("Сколько будет 25 * 4?")
    print("\n" + "="*50 + "\n")
    run_agent("Который час в Москве?")