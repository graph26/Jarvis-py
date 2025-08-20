import threading

from art import tprint
import openwakeword
import numpy as np
from funct.fun import *
from recognition import *
import time
from funct.stack import *

running = True
start_time = 0
live = True  # Для отключения цикла (программы)
# Автоматическая загрузка доступных моделей
openwakeword.utils.download_models()

# Создание детектора
owwModel = openwakeword.Model(
    wakeword_models=[
        'alexa',
        'hey_jarvis',
        './wake_word/jarvis.onnx'
    ],
    vad_threshold=0.95,  # Порог увереннсти
    inference_framework='onnx'
)

# Настройка аудио
CHUNK = 1280  # Размер чанка для openwakeword
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Инициализация PyAudio
p = pyaudio.PyAudio()

# Открытие аудио потока
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print(f"Available models: {list(owwModel.models.keys())}")


def respond_to_user():
    global recognizer, microphone, start_time, live

    with microphone as source:
        text_start = "[Jarvis]: Ready to receive the team..."
        print(text_start)
        recognizer.adjust_for_ambient_noise(source, duration=2)

    while live:
        with microphone as source:
            audio = recognizer.listen(source, phrase_time_limit=5)
        command = ''
        try:
            command = faster_whisper_recognition(audio)
            print('Commands:', command)
            # Здесь можно добавить обработку команд
            if 'выключись' in command:
                perform_audio('Отключаю питание')
                live = False
                eel.exit_frontend()
                exit()

            elif any(com in command for com in ['звук', 'громкость', 'тише', 'громче']):
                if any(com in command for com in ['уменьши', 'понись', 'понизить', 'тише']):
                    pyautogui.press('volumedown')
                    print("[Jarvis]: Valume down")
                    perform_audio('Запрос выполнен сэр')
                    listen_for_hotword()
                elif any(com in command for com in ['увеличь', 'повысь', 'увеличить', 'громче']):
                    pyautogui.press('volumeup')
                    print("[Jarvis]: Valume up")
                    perform_audio('Запрос выполнен сэр')
                    listen_for_hotword()
            else:
                command_function(command)
                print(f'--seconds--: {(time.perf_counter() - start_time):.2f}')
                listen_for_hotword()

        except:
            print("[Jarvis]: The command could not be recognized")
            listen_for_hotword()


def listen_for_hotword():
    global start_time, live
    print("Expectation wake words...")

    try:
        while live:
            # Чтение аудио данных
            audio_data = stream.read(CHUNK)

            # Конвертация в numpy array
            audio_data = np.frombuffer(audio_data, dtype=np.int16)

            # Предсказание
            prediction = owwModel.predict(audio_data)

            # Проверка результатов
            for wakeword, confidence in prediction.items():
                # print(confidence)
                if confidence > 0.98:
                    print(f" Detected '{wakeword}' with confidence {confidence:.2f}")
                    start_time = time.perf_counter()
                    respond_to_user()

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()


# Функция для проигрывания стартового звука
def play_startup_sound():
    with wave.open('Jarvis Sound Pack/Доброе утро.wav', 'rb') as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)
    stream = p.open(
        format=p.get_format_from_width(params.sampwidth),
        channels=params.nchannels,
        rate=params.framerate,
        output=True
    )
    stream.write(frames)


def on_close(page, sockets):
    global live
    live = False
    print("[Jarvis]: Exit")
    exit()


if __name__ == "__main__":
    tprint("FriDay")
    threading.Thread(target=play_startup_sound, daemon=True).start()

    threading.Thread(target=listen_for_hotword, daemon=True).start()
    # listen_for_hotword()
    eel.init('GUI')
    eel.start('./jarvis.html', size=(556, 703), shutdown_delay=0.5)
