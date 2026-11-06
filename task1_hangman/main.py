
import random


WORDS = ["PYTHON", "COMPUTER", "SECURITY", "NETWORK", "HACKER"]
MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
========= 
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
========= 
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
========= 
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
========= 
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
========= 
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
========= 
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
========= 
""",
]


def display_gallows(incorrect_guesses):
    """Display the gallows for the current number of mistakes."""
    print(HANGMAN_STAGES[incorrect_guesses])


def display_word(secret_word, guessed_letters):
    """Show correctly guessed letters and mask the remaining ones."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_hangman():
    """Run one complete round of Hangman."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("=== Welcome to Hangman! ===")
    print(f"The word has {len(secret_word)} letters.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_gallows(incorrect_guesses)

        print("Word:", display_word(secret_word, guessed_letters))

        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").strip().upper()

        # Accept exactly one English alphabetic letter.
        if len(guess) != 1 or guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Invalid input. Enter one letter from A to Z.")
            continue

        # A repeated guess must not count as another mistake.
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print(
                f"Incorrect guess! "
                f"{MAX_INCORRECT_GUESSES - incorrect_guesses} "
                f"attempts remaining."
            )

        # Check whether every letter in the word has been revealed.
        if all(letter in guessed_letters for letter in secret_word):
            display_gallows(incorrect_guesses)
            print("Word:", display_word(secret_word, guessed_letters))
            print("Congratulations! You won!")
            return

    # The player has used all six incorrect guesses.
    display_gallows(incorrect_guesses)
    print("You lost! The correct word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
