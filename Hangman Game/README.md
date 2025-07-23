# Hangman Game 🎮

A simple command-line implementation of the classic Hangman game in Python.

## Features

* Random word selection from a predefined list
* User input for guessing letters
* Displays the current progress of the guessed word
* Tracks incorrect guesses (up to 6 allowed)
* Displays guessed letters so far
* Game over messages (win or lose)

## How to Play

1. Run the Python script using any Python 3 interpreter.
2. The program will randomly select a word from the list.
3. You'll guess one letter at a time.
4. If the letter is correct, it will be revealed in the word.
5. You have a maximum of 6 incorrect guesses.
6. The game ends when:

   * You guess the word correctly.
   * You run out of incorrect guesses.

## Requirements

* Python 3.x

## Running the Game

```bash
python hangman.py
```

## Example

```
Welcome to Hangman! 🎮
The word has 6 letters.

Word: _ _ _ _ _ _
Incorrect guesses left: 6
Guessed letters:
Guess a letter: p
Good guess! 'p' is in the word.
```

## Customization

You can modify the list of words by editing the `words` list in the script:

```python
words = ["python", "hangman", "computer", "program", "game"]
```

---

Happy Coding! 🚀
