import random

def hangman():
    words = ["python", "developer", "hima", "bindu", "india", "coding", "chatgpt"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("Welcome to the Hangman Game!")
    print("_ " * len(word))  # First time underscores

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        if display_word.replace(" ", "") == word:
            print("\n🎉 Congratulations! You guessed the word correctly:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("✅ Correct guess!")
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f"❌ Wrong guess! Attempts left: {attempts}")

    if attempts == 0:
        print("\n😢 Game Over! The word was:", word)

# Run the game
hangman()
