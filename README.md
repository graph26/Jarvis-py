# Jarvis-py

`Jarvis` - is a voice assistant made as an experiment using neural networks for things like **STT/TTS/Wake Word** etc.

The main project challenges we try to achieve is:
 - 100% offline *(no cloud)*
 - Open source *(full transparency)*
 - No data collection *(we respect your privacy)*

Our backend stack is 🐍 **[Python](https://www.rust-lang.org/)** with ❤️ **[Eel](https://pypi.org/project/Eel/)**.<br>
For the frontend we use ⚡️ **HTML & CSS** + 🛠️ **JS**.

# JARVIS Voice Assistant

![We are NOT limited by the technology of our time!](poster.jpg)

`Jarvis` - is a voice assistant made as an experiment using neural networks for things like **STT/TTS/Wake Word/NLU** etc.

The main project challenges we try to achieve is:
 - 100% offline *(no cloud)*
 - Open source *(full transparency)*
 - No data collection *(we respect your privacy)*

Our backend stack is 🦀 **[Rust](https://www.rust-lang.org/)** with ❤️ **[Tauri](https://tauri.app/)**.<br>
For the frontend we use ⚡️ **[Vite](https://vitejs.dev/)** + 🛠️ **[Svelte](https://svelte.dev/)**.

*Other libraries, tools and packages can be found in source code.*

## Neural Networks

This are the neural networks we are currently using:

- Speech-To-Text
	- [~~Vosk Speech Recognition Toolkit~~](https://github.com/alphacep/vosk-api) via [Vosk](https://github.com/alphacep/vosk-api/tree/master/python) *(currently not used)*
    - [Faster-Wishper](https://github.com/SYSTRAN/faster-whisper?ysclid=mejrq9wlb9541488105)
- Text-To-Speech
	- [~~Silero TTS~~](https://github.com/snakers4/silero-models) *(currently not used)*
	- [~~Coqui TTS~~](https://github.com/coqui-ai/TTS) *(currently not used)*
	- [~~gTTS~~](https://github.com/nightlyistaken/tts_rust) *(currently not used)*
- Wake Word
	- [OpenWakeWord](https://github.com/dscripka/openWakeWord)
	- [~~Picovoice Porcupine~~](https://github.com/Picovoice/porcupine) via [official SDK](https://github.com/Picovoice/porcupine#rust) *(requires API key)*
	- [~~Vosk Speech Recognition Toolkit~~](https://github.com/alphacep/vosk-api) via [Vosk](https://github.com/alphacep/vosk-api/tree/master/python) *(very slow & currently not used)*

## Supported Languages

Currently, only Russian language is supported.<br>
But soon, English will be added for the interface, wake-word detection and speech recognition.

## Author

graph26

## License

[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
See LICENSE.txt file for more details.
