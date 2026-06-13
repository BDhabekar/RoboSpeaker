# config.py — Central configuration for RoboSpeaker

# TTS Settings
TTS_RATE = 150          # Words per minute (default: 150)
TTS_VOLUME = 1.0        # Volume: 0.0 to 1.0
TTS_VOICE_INDEX = 0     # 0 = first available voice (usually male), 1 = female

# App Info
APP_NAME = "RoboSpeaker"
APP_VERSION = "1.0.0"

# Future: STT Settings (used when upgrading to voice assistant)
STT_LANGUAGE = "en-US"
STT_TIMEOUT = 5         # seconds to wait for speech
STT_PHRASE_LIMIT = 10   # max seconds to record a phrase
