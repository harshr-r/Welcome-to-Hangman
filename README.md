# Hangman Game

A simple Hangman game implemented in Python.

## Features
- Play the classic Hangman game in the terminal
- Random word selection from a predefined list
- ASCII art for different stages of the game
- Interactive guessing with feedback

## Files
- `hangman.py` - Main game logic
- `hangman_images.py` - ASCII art for Hangman stages

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   cd hangman-game
   ```
2. Run the game:
   ```bash
   python hangman.py
   ```

## How to Play
- The game selects a random word.
- You guess letters one by one.
- If you guess incorrectly, a part of the hangman is drawn.
- You have 6 incorrect guesses before the game ends.
- Guess all letters correctly to win!

## Example Output
```
Welcome to Hangman!
       +---+
       |   |
           |
           |
           |
           |
    =========
_ _ _ _ _ _
Guess a letter:
```
