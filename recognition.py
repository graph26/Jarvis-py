import speech_recognition as sr
from faster_whisper import WhisperModel
import GPUtil
import os

# Initialize model with desired size and device
model = WhisperModel("./models/whisper-small", device="cuda" if len(GPUtil.getGPUs()) > 0 else "cpu",
                     compute_type="float16" if len(GPUtil.getGPUs()) > 0 else "int8")

recognizer = sr.Recognizer()
microphone = sr.Microphone()


def faster_whisper_recognition(audio_data) -> str:
    """Распознавание через Faster Whisper"""
    try:
        # Сохраняем аудио во временный WAV файл
        temp_filename = "temp_audio.wav"
        with open(temp_filename, "wb") as f:
            f.write(audio_data.get_wav_data())

        # Распознаем через Faster Whisper
        segments, info = model.transcribe(
            temp_filename
        )
        # Собираем текст из всех сегментов
        text = " ".join([segment.text.strip() for segment in segments])
        # Удаляем временный файл
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

        return text.lower()

    except Exception as e:
        print(f"Ошибка распознавания: {e}")
        return ""
