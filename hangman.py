import random

def hangman():
    words = ['python', 'internship', 'codealpha', 'programming', 'github']
    word = random.choice(words)
    guesses = ''
    turns = 6

    print("Welcome to the Hangman Game!")
    print("Guess the word one letter at a time.")
    print("_ " * len(word))

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1

        print()

        if failed == 0:
            print("\nCongratulations! You won!")
            print(f"The word was: {word}")
            break

        guess = input("Guess a letter: ")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong guess.")
            print(f"You have {turns} turns left.")

            if turns == 0:
                print("\nGame Over! You lose.")
                print(f"The word was: {word}")

hangman()
