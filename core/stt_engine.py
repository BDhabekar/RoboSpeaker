# core/stt_engine.py — Speech-to-Text engine (stub for v2 voice assistant upgrade)

# Uncomment and implement this when upgrading RoboSpeaker to a voice assistant.
#
# import speech_recognition as sr
# from config import STT_LANGUAGE, STT_TIMEOUT, STT_PHRASE_LIMIT
# from utils.logger import get_logger
#
# logger = get_logger(__name__)
#
#
# class STTEngine:
#     """
#     Wraps SpeechRecognition for microphone-based speech input.
#     Can be swapped with Whisper (OpenAI) for better accuracy later.
#     """
#
#     def __init__(self):
#         self._recognizer = sr.Recognizer()
#         self._mic = sr.Microphone()
#
#     def listen(self) -> str:
#         """Listen from mic and return transcribed text."""
#         with self._mic as source:
#             logger.info("Adjusting for ambient noise...")
#             self._recognizer.adjust_for_ambient_noise(source, duration=1)
#             logger.info("Listening...")
#             audio = self._recognizer.listen(
#                 source,
#                 timeout=STT_TIMEOUT,
#                 phrase_time_limit=STT_PHRASE_LIMIT
#             )
#         try:
#             text = self._recognizer.recognize_google(audio, language=STT_LANGUAGE)
#             logger.info(f"Heard: {text}")
#             return text
#         except sr.UnknownValueError:
#             logger.warning("Could not understand audio.")
#             return ""
#         except sr.RequestError as e:
#             logger.error(f"STT API error: {e}")
#             return ""

# Placeholder so imports don't break in v1
class STTEngine:
    def listen(self) -> str:
        raise NotImplementedError("STT not implemented yet. Upgrade to v2.")
