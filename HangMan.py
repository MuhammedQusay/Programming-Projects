import random
from os import system

def draw_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    print(stages[attempts])

def hangman():
    words = ["python", "programming", "hangman", "challenge", "developer", "algorithm"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    word_completion = "_ " * len(word)
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {attempts} attempts to guess it.")
    print(word_completion)
    draw_hangman(attempts)
    
    while attempts > 0:

        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            system("cls||clear")
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            system("cls||clear")
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            system("cls||clear")
            print(f"Good job! '{guess}' is in the word.")
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
            print(word_completion)
        else:
            system("cls||clear")
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")
            print(word_completion)
            draw_hangman(attempts)
        
        if "_" not in word_completion:
            system("cls||clear")
            print("Congratulations! You guessed the word:", word)
            break
    
    if attempts == 0:
        system("cls||clear")
        draw_hangman(0)
        print("You ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
