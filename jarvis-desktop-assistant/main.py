#!/usr/bin/env python3
"""
Jarvis Desktop Assistant - Main Entry Point
Windows 11 | Python 3.x | Groq AI Backend
"""

import os
import sys
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Load environment variables
load_dotenv()
init(autoreset=True)

from jarvis.brain import Brain
from jarvis.voice import Voice
from jarvis.commands import CommandHandler

BANNER = f"""
{Fore.CYAN}
     _    _    ____  __     __ ___ ____  
    | |  / \  |  _ \ \ \   / /|_ _/ ___| 
 _  | | / _ \ | |_) | \ \ / /  | |\___ \ 
| |_| |/ ___ \|  _ <   \ V /   | | ___) |
 \___//_/   \_\_| \_\   \_/   |___|____/ 
{Style.RESET_ALL}
{Fore.YELLOW}  Your AI Desktop Assistant - Powered by Groq{Style.RESET_ALL}
{Fore.WHITE}  Say 'Hey Jarvis' or type your command below{Style.RESET_ALL}
"""

def main():
    print(BANNER)

    # Initialize components
    brain = Brain()
    voice = Voice()
    commands = CommandHandler()

    print(f"{Fore.GREEN}✓ AI Brain loaded ({brain.backend} / {brain.model}){Style.RESET_ALL}")
    print(f"{Fore.GREEN}✓ Voice engine ready{Style.RESET_ALL}")
    print(f"{Fore.GREEN}✓ Command handler ready{Style.RESET_ALL}")
    print(f"\n{Fore.CYAN}Type your command or press ENTER to use voice input.{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Type 'quit' to exit.{Style.RESET_ALL}\n")

    while True:
        try:
            user_input = input(f"{Fore.YELLOW}You: {Style.RESET_ALL}").strip()

            if not user_input:
                # Voice input
                print(f"{Fore.CYAN}Listening...{Style.RESET_ALL}")
                user_input = voice.listen()
                if not user_input:
                    print(f"{Fore.RED}Could not hear anything. Try again.{Style.RESET_ALL}")
                    continue
                print(f"{Fore.YELLOW}You (voice): {user_input}{Style.RESET_ALL}")

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"{Fore.CYAN}Jarvis: Goodbye! Have a great day!{Style.RESET_ALL}")
                voice.speak("Goodbye! Have a great day!")
                sys.exit(0)

            # Check for built-in commands first
            cmd_response = commands.handle(user_input)
            if cmd_response:
                print(f"{Fore.CYAN}Jarvis: {cmd_response}{Style.RESET_ALL}")
                voice.speak(cmd_response)
                continue

            # Send to AI brain
            response = brain.chat(user_input)
            print(f"{Fore.CYAN}Jarvis: {response}{Style.RESET_ALL}")
            voice.speak(response)

        except KeyboardInterrupt:
            print(f"\n{Fore.CYAN}Jarvis: Goodbye!{Style.RESET_ALL}")
            sys.exit(0)
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
