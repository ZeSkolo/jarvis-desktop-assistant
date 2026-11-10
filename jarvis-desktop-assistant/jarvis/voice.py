"""
Jarvis Voice - Speech Recognition + Text to Speech
"""

import os
import sys

class Voice:
    def __init__(self):
        self.enabled = os.getenv("JARVIS_VOICE", "enabled").lower() == "enabled"
        self.tts_engine = None
        self.recognizer = None
        self._init_tts()
        self._init_stt()

    def _init_tts(self):
        try:
            import pyttsx3
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', 175)   # speed
            self.tts_engine.setProperty('volume', 0.9)
            # Try to set a good Windows voice
            voices = self.tts_engine.getProperty('voices')
            for voice in voices:
                if 'david' in voice.name.lower() or 'zira' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
        except Exception as e:
            print(f"[Voice] TTS not available: {e}")
            self.tts_engine = None

    def _init_stt(self):
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.sr = sr
        except Exception as e:
            print(f"[Voice] Speech recognition not available: {e}")
            self.recognizer = None

    def speak(self, text: str):
        """Convert text to speech"""
        if not self.enabled or not self.tts_engine:
            return
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"[Voice] TTS error: {e}")

    def listen(self, timeout: int = 5) -> str:
        """Listen for voice input and return transcribed text"""
        if not self.recognizer:
            return ""
        try:
            with self.sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
            text = self.recognizer.recognize_google(audio)
            return text
        except self.sr.WaitTimeoutError:
            return ""
        except self.sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"[Voice] Listen error: {e}")
            return ""
