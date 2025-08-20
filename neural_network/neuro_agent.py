from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain import HuggingFaceHub

llm = HuggingFaceHub()
