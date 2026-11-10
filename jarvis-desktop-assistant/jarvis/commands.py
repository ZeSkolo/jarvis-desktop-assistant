"""
Jarvis Commands - Built-in Windows commands handler
"""

import os
import subprocess
import datetime
import psutil

class CommandHandler:
    def __init__(self):
        self.commands = {
            # App launchers
            "open chrome": lambda: self._open_app("chrome"),
            "open notepad": lambda: self._open_app("notepad"),
            "open calculator": lambda: self._open_app("calc"),
            "open file explorer": lambda: self._open_app("explorer"),
            "open task manager": lambda: self._open_app("taskmgr"),
            "open vs code": lambda: self._open_app("code"),
            "open terminal": lambda: self._open_app("wt"),
            # System info
            "what time is it": self._get_time,
            "what's the time": self._get_time,
            "whats the time": self._get_time,
            "what day is it": self._get_date,
            "what's the date": self._get_date,
            "battery status": self._get_battery,
            "cpu usage": self._get_cpu,
            "ram usage": self._get_ram,
            "system info": self._get_system_info,
            # Jarvis control
            "clear memory": lambda: "Use brain.reset_memory() to clear my memory.",
            "help": self._get_help,
        }

    def handle(self, user_input: str) -> str | None:
        """Check if input matches a built-in command. Returns response or None."""
        normalized = user_input.lower().strip()
        for cmd, handler in self.commands.items():
            if cmd in normalized:
                return handler()
        return None

    def _open_app(self, app: str) -> str:
        try:
            subprocess.Popen(app, shell=True)
            return f"Opening {app}!"
        except Exception as e:
            return f"Could not open {app}: {e}"

    def _get_time(self) -> str:
        now = datetime.datetime.now()
        return f"It's {now.strftime('%I:%M %p')}."

    def _get_date(self) -> str:
        now = datetime.datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}."

    def _get_battery(self) -> str:
        try:
            battery = psutil.sensors_battery()
            if battery:
                status = "charging" if battery.power_plugged else "discharging"
                return f"Battery is at {battery.percent:.0f}% and {status}."
            return "No battery detected (desktop PC?)."
        except:
            return "Could not read battery status."

    def _get_cpu(self) -> str:
        usage = psutil.cpu_percent(interval=1)
        return f"CPU usage is at {usage}%."

    def _get_ram(self) -> str:
        mem = psutil.virtual_memory()
        used = mem.used / (1024**3)
        total = mem.total / (1024**3)
        return f"RAM usage: {used:.1f} GB used out of {total:.1f} GB ({mem.percent}%)."

    def _get_system_info(self) -> str:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        ram_used = mem.used / (1024**3)
        ram_total = mem.total / (1024**3)
        return (
            f"CPU: {cpu}% | "
            f"RAM: {ram_used:.1f}/{ram_total:.1f} GB ({mem.percent}%)"
        )

    def _get_help(self) -> str:
        return (
            "Built-in commands: open chrome/notepad/calculator/file explorer/vs code/terminal, "
            "what time is it, what day is it, battery status, cpu usage, ram usage, system info. "
            "For everything else, I'll ask my AI brain!"
        )
