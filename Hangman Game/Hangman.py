import random

def play_hangman():
    words = ["python", "hangman", "computer", "program", "game"]
    word_to_guess = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman! 🎮")
    print(f"The word has {len(word_to_guess)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {word_to_guess} 🎉")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    else:
        print(f"\nGame Over! You ran out of guesses. The word was: {word_to_guess} 💀")

if __name__ == "__main__":
    play_hangman()
