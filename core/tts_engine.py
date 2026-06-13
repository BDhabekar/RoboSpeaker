# core/tts_engine.py — Text-to-Speech engine abstraction

import pyttsx3
from config import TTS_RATE, TTS_VOLUME, TTS_VOICE_INDEX
from utils.logger import get_logger

logger = get_logger(__name__)


class TTSEngine:
    """
    Wraps pyttsx3 for offline TTS.
    Designed to be swappable — replace pyttsx3 with ElevenLabs or
    Google Cloud TTS later without changing any other module.
    """

    def __init__(self):
        self._engine = pyttsx3.init()
        self._apply_config()

    def _apply_config(self):
        """Apply settings from config.py."""
        self._engine.setProperty("rate", TTS_RATE)
        self._engine.setProperty("volume", TTS_VOLUME)

        voices = self._engine.getProperty("voices")
        if voices and TTS_VOICE_INDEX < len(voices):
            self._engine.setProperty("voice", voices[TTS_VOICE_INDEX].id)
            logger.info(f"Voice set to: {voices[TTS_VOICE_INDEX].name}")

    def speak(self, text: str):
        """Convert text to speech and play it."""
        if not text.strip():
            logger.warning("speak() called with empty text.")
            return
        logger.info(f"Speaking: {text[:60]}...")
        self._engine.say(text)
        self._engine.runAndWait()

    def set_rate(self, rate: int):
        """Dynamically adjust speech rate."""
        self._engine.setProperty("rate", rate)

    def set_volume(self, volume: float):
        """Dynamically adjust volume (0.0 - 1.0)."""
        self._engine.setProperty("volume", volume)

    def get_available_voices(self) -> list:
        """Return list of available voice names."""
        voices = self._engine.getProperty("voices")
        return [v.name for v in voices] if voices else []

    def stop(self):
        """Stop any ongoing speech."""
        self._engine.stop()
