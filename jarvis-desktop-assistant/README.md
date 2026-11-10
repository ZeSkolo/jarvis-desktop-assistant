# 🤖 Jarvis Desktop Assistant

Your personal AI-powered desktop assistant for Windows 11, built with Python and Groq AI.

## ✨ Features

- 🧠 **AI Brain** — Groq (Llama 3), Gemini, or Ollama (offline)
- 🎙️ **Voice Input** — Speak your commands
- 🔊 **Voice Output** — Jarvis talks back
- ⚡ **Built-in Commands** — Open apps, check time, battery, CPU/RAM
- 💬 **Conversation Memory** — Remembers context across messages
- 🔌 **Offline Mode** — Works with Ollama (no internet needed)

## 🚀 Quick Start

### 1. Install
```bash
# Double-click install.bat  OR  run:
pip install -r requirements.txt
```

### 2. Configure
```bash
copy .env.example .env
# Open .env in Notepad and add your Groq API key
```

Get a free Groq API key at: https://console.groq.com

### 3. Run
```bash
python main.py
```

## 🎮 How to Use

| Input | Action |
|-------|--------|
| Type your message | Text mode |
| Press ENTER (empty) | Voice mode |
| `quit` / `exit` | Close Jarvis |

## 🗣️ Built-in Commands

| Command | Action |
|---------|--------|
| `open chrome` | Opens Chrome |
| `open notepad` | Opens Notepad |
| `open calculator` | Opens Calculator |
| `open file explorer` | Opens Explorer |
| `open vs code` | Opens VS Code |
| `open terminal` | Opens Windows Terminal |
| `what time is it` | Current time |
| `what day is it` | Current date |
| `battery status` | Battery % |
| `cpu usage` | CPU % |
| `ram usage` | RAM usage |
| `system info` | CPU + RAM summary |
| `help` | List all commands |

## ⚙️ Configuration (.env)

```env
GROQ_API_KEY=your_key_here        # Get free from console.groq.com
AI_BACKEND=groq                   # groq / gemini / ollama
GROQ_MODEL=llama-3.1-8b-instant   # or llama-3.3-70b-versatile
JARVIS_VOICE=enabled              # enabled / disabled
```

## 🔄 AI Backend Options

| Backend | Speed | Cost | Offline |
|---------|-------|------|--------|
| **Groq** | ⚡ Fastest | Free | No |
| **Gemini** | Fast | Free | No |
| **Ollama** | Medium | Free | ✅ Yes |

## 📁 Project Structure

```
jarvis-desktop-assistant/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── install.bat          # Windows installer
├── .env.example         # Config template
└── jarvis/
    ├── brain.py         # AI backend (Groq/Gemini/Ollama)
    ├── voice.py         # Speech recognition + TTS
    └── commands.py      # Built-in Windows commands
```

## 🛠️ Requirements

- Windows 11 (64-bit)
- Python 3.9+
- 16GB RAM (recommended)
- Microphone (for voice mode)
- Internet (for Groq/Gemini) or Ollama installed (offline)

## 🆓 Free API Keys

- **Groq**: https://console.groq.com (14,400 req/day free)
- **Gemini**: https://aistudio.google.com (1,500 req/day free)
- **Ollama**: https://ollama.com (fully local, unlimited)
