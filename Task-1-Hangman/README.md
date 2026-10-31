# Hangman Word Guessing Game (Console)

A Python-based interactive Hangman game where players attempt to guess a randomly selected hidden English word, one letter at a time, within six incorrect attempts.

## Features

- Random English word selection from an external word list.
- Interactive command-line gameplay.
- ASCII-based visual gallows that update after incorrect guesses.
- Displays correctly guessed letters and masks unrevealed letters.
- Tracks previously guessed letters.
- Prevents duplicate guesses from deducting attempts.
- Validates user input.
- Displays victory and defeat messages.
- Reveals the secret word when the player loses.

## Technologies Used

- Python 3
- Random Module
- Standard Python Libraries
- VS Code / PyCharm

## Project Structure

```text
Hangman-Word-Guessing-Game/
│
├── hangman.py
├── word-list.txt
└── README.md
```

## Requirements

- Python 3.x installed.
- English word list (`word-list.txt`).
- No external Python packages required.

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/Aymanaahh/Hangman-Word-Guessing-Game
```

**2. Navigate to the project directory**

```bash
cd Hangman-Word-Guessing-Game
```

**3. Run the game**

```bash
python hangman.py
```

Make sure `word-list.txt` is in the same directory as `hangman.py`.

## How to Play

1. Run the Python program.
2. The game randomly selects a secret English word.
3. Enter one letter at a time to guess the word.
4. Correct guesses reveal the corresponding letters.
5. Incorrect guesses update the ASCII gallows and consume one attempt.
6. You have a maximum of six incorrect attempts.
7. Guess the complete word to win!

## Learning Outcomes

This project demonstrates practical implementation of:

- Python string manipulation.
- Conditional statements and loops.
- Lists, sets, and random selection.
- User input validation.
- File handling.
- Functions and modular programming.
- Basic game logic and state management.

## Author

Developed as part of a Python programming assignment.

---

**Note:** This project uses Python's standard library and does not require additional dependencies.