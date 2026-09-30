🎯 Number Guessing Game

A simple Python Number Guessing Game where the player gets 3 chances to guess a randomly generated number between 1 and 10.

🎮 How the Game Works

1. The computer randomly selects a number between 1 and 10.
2. The player gets 3 chances to guess the number.
3. After each incorrect guess, the remaining attempts are displayed.
4. If the player guesses correctly, they win the game.
5. If all 3 guesses are incorrect, the player loses and the correct number is revealed.

✨ Features

- 🎲 Random number generation
- 🔢 Number range from 1 to 10
- ❤️ 3 guessing attempts
- 🏆 Win/Lose messages
- ⏱️ Displays a game time value after winning
- 😄 Fun ASCII-art messages
- ⏳ One-second delay between guesses

🛠️ Requirements

- Python 3.x
- No external libraries are required.

The program uses Python's built-in modules:

import random
import time
import math

🚀 How to Run

1. Clone the repository

git clone <your-repository-url>

2. Open the project folder

cd <project-folder>

3. Run the Python program

python main.py

Depending on your system, you may need:

python3 main.py

🕹️ Example Gameplay

================================
       GAMBLE AT YOUR OWN RISK
================================
You have 3 chances to guess the number.

Your guess is: 5
YOUR GUESS WAS WRONG
YOU HAVE 2 GUESSES LEFT

Your guess is: 7
YOU WON!!! HEE - YAAA

             ♫      *\O*/     ♫
                    |
                   / *\*   <3

You guessed the number correctly!
Game finished in 42 seconds.

📂 Project Structure

number-guessing-game/
│
├── main.py
└── README.md

🧠 Concepts Used

This project is useful for practicing basic Python concepts such as:

- Functions
- "while" loops
- "if/else" conditions
- User input
- Variables
- Random number generation
- String formatting
- Python modules
- "break"
- Basic time handling

⚠️ Note

The program expects the user to enter a valid integer. Entering text or a non-integer value will cause a "ValueError".

📜 License

This project is open for learning and personal use.