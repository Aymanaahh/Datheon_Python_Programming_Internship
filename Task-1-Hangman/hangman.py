import random

# 1. Load the word list
def load_words():
    with open("word-list.txt", "r") as file:
        wordList = [
            word.strip().lower()
            for word in file
            if word.strip().isalpha()
        ]

    return wordList


# 2. Display the ASCII gallows
def display_gallows(mistakes):
    stages = [
        """
         +---+
         |   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
        =========
        """
    ]

    print(stages[mistakes])


# 3. Display the current game status
def display_game(secretWord, guessed_letters, mistakes):
    display_gallows(mistakes)

    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secretWord
    )

    print("\nWord:", display)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Attempts remaining:", 6 - mistakes)


# 4. Get and validate the player's guess
def get_guess(guessed_letters):
    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter exactly one English letter.")
        return None

    if guess in guessed_letters:
        print("You already guessed that letter!")
        return None

    return guess


# 5. Main game function
def play_game():
    wordList = load_words()

    if not wordList:
        print("Error: Word list is empty or unavailable.")
        return

    secretWord = random.choice(wordList)

    guessed_letters = set()
    mistakes = 0
    max_attempts = 6

    print("Welcome to Hangman!")

    while mistakes < max_attempts:

        # Display current game status
        display_game(secretWord, guessed_letters, mistakes)

        # Get player's input
        guess = get_guess(guessed_letters)

        if guess is None:
            continue

        # Track the guessed letter
        guessed_letters.add(guess)

        # Check whether the guess is correct
        if guess in secretWord:
            print("Correct guess!")
        else:
            mistakes += 1
            print("Incorrect guess!")

        # Check for a win
        if all(letter in guessed_letters for letter in secretWord):
            print("\n" + secretWord)
            print("Congratulations! You won!")
            return

    # Check for a loss
    display_gallows(mistakes)
    print("Game over! You ran out of attempts.")
    print("The secret word was:", secretWord)


# 6. Start the game
if __name__ == "__main__":
    play_game()
