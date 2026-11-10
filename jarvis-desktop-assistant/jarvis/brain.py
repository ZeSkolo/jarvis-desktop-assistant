"""
Jarvis Brain - AI Backend (Groq / Gemini / Ollama)
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Brain:
    def __init__(self):
        self.backend = os.getenv("AI_BACKEND", "groq").lower()
        self.history = [
            {"role": "system", "content": (
                "You are Jarvis, a smart, friendly, and efficient desktop assistant for Windows 11. "
                "You help the user with tasks, answer questions, open apps, manage files, and more. "
                "Keep responses concise and actionable. Use a helpful, slightly witty tone."
            )}
        ]

        if self.backend == "groq":
            self._init_groq()
        elif self.backend == "gemini":
            self._init_gemini()
        elif self.backend == "ollama":
            self._init_ollama()
        else:
            raise ValueError(f"Unknown AI_BACKEND: {self.backend}")

    def _init_groq(self):
        from groq import Groq
        self.model = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def _init_gemini(self):
        import google.generativeai as genai
        self.model = "gemini-1.5-flash"
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.client = genai.GenerativeModel(self.model)
        self._gemini_chat = self.client.start_chat(history=[])

    def _init_ollama(self):
        import requests
        self.model = os.getenv("OLLAMA_MODEL", "llama3.1")
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.client = requests  # use requests directly

    def chat(self, user_message: str) -> str:
        try:
            if self.backend == "groq":
                return self._chat_groq(user_message)
            elif self.backend == "gemini":
                return self._chat_gemini(user_message)
            elif self.backend == "ollama":
                return self._chat_ollama(user_message)
        except Exception as e:
            return f"Sorry, I ran into an error: {e}"

    def _chat_groq(self, message: str) -> str:
        self.history.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            max_tokens=512,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        # Keep history manageable (last 20 messages + system)
        if len(self.history) > 21:
            self.history = [self.history[0]] + self.history[-20:]
        return reply

    def _chat_gemini(self, message: str) -> str:
        response = self._gemini_chat.send_message(message)
        return response.text

    def _chat_ollama(self, message: str) -> str:
        self.history.append({"role": "user", "content": message})
        response = self.client.post(
            f"{self.base_url}/api/chat",
            json={"model": self.model, "messages": self.history, "stream": False}
        )
        reply = response.json()["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def reset_memory(self):
        """Clear conversation history (keep system prompt)"""
        self.history = [self.history[0]]
        return "Memory cleared!"
