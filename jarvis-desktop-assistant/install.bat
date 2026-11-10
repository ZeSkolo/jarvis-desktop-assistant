@echo off
echo ============================================
echo  Jarvis Desktop Assistant - Windows Installer
echo ============================================
echo.

echo [1/4] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Download from https://python.org
    pause
    exit /b 1
)
python --version
echo.

echo [2/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)
echo.

echo [3/4] Setting up .env file...
if not exist .env (
    copy .env.example .env
    echo Created .env file. Please open it and add your API key!
) else (
    echo .env already exists, skipping.
)
echo.

echo [4/4] Done!
echo.
echo ============================================
echo  HOW TO START JARVIS:
echo  1. Open .env and paste your Groq API key
echo  2. Run:  python main.py
echo ============================================
echo.
pause
