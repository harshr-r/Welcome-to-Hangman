import random
from hangman_images import hangman_stages

def get_word():
    words = ['python', 'java', 'javascript', 'hangman', 'computer', 'developer']
    return random.choice(words).upper()

def display(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(hangman_stages[6 - attempts])
        print(display(word, guessed_letters))
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) <= guessed_letters:
                print("Congratulations! You guessed the word:", word)
                return
        else:
            attempts -= 1
            print("Incorrect! Attempts left:", attempts)
        
    print(hangman_stages[6])
    print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
