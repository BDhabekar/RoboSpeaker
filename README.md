# 🤖 RoboSpeaker

A lightweight, offline Text-to-Speech desktop app built with Python.
Designed to be easily upgraded into a full voice assistant.

## Features (v1)
- Offline TTS via `pyttsx3`
- Adjustable speech rate and volume
- Long-text chunking for smooth playback
- Non-blocking UI (TTS runs in background thread)

## Setup

```bash
pip install -r requirements.txt
python main.py
```

> **Note:** `pyaudio` may need system-level install on some platforms:
> - Ubuntu/Debian: `sudo apt install portaudio19-dev`
> - Windows: install via pip usually works directly

## Project Structure

```
RoboSpeaker/
├── main.py              # Entry point
├── config.py            # Central config (rate, volume, voice)
├── requirements.txt
├── core/
│   ├── tts_engine.py    # TTS abstraction (pyttsx3)
│   └── stt_engine.py    # STT stub (for v2 voice assistant)
├── ui/
│   └── app_window.py    # Tkinter UI
└── utils/
    ├── logger.py         # Logging setup
    └── helpers.py        # Text sanitization & chunking
```

## Upgrading to Voice Assistant (v2)

1. Uncomment `core/stt_engine.py` and implement `STTEngine.listen()`
2. Add a "Listen" button in `ui/app_window.py`
3. Connect STT output → LLM (LangChain) → TTS pipeline
4. Optionally add wake word detection via `pvporcupine`
