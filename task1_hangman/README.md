# Task 1: Hangman Game

## Overview
Hangman is a command-line word-guessing game developed using Python. The player must guess a hidden word one letter at a time before making six incorrect guesses.

## Features
- Random word selection from a predefined list.
- Displays hidden letters as underscores.
- Accepts one English alphabet letter at a time.
- Rejects invalid inputs.
- Detects and prevents repeated guesses from counting as mistakes.
- Displays the number of incorrect guesses remaining.
- Shows win and loss messages.
- Reveals the correct word when the player loses.

## Requirements
- Python 3.10 or later
- A terminal or command prompt

## How to Run

1. Open a terminal in the `task1_hangman` folder.
2. Run the following command:

```bash
python main.py
```

3. Enter one letter at a time when prompted.
4. Guess all the letters before reaching six incorrect guesses to win.

## How to Play
- Enter a single letter from A to Z.
- Correct guesses reveal the matching letters.
- Incorrect guesses reduce the remaining attempts.
- Invalid inputs and repeated guesses do not consume an attempt.
- The game ends when you guess the word or use all six incorrect guesses.

## Concepts Used
- Variables and constants
- Lists and sets
- Loops and conditional statements
- Functions
- Random selection
- String methods and input validation

## Project Structure

```text
task1_hangman/
├── main.py
├── README.md
└── TEST_REPORT.md
```

## Author
Developed as part of the Datheon Python Programming Internship.