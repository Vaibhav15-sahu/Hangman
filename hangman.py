import random
from words import words
import string

def hangman():
    word = random.choice(words).upper()
    while '-' in word or ' ' in word :
        word = random.choice(words).upper()

    letters = set(word)
    gussed_letters = []

    lives = 7

    while lives > 0 and len(gussed_letters) < len(letters) :
        curr_word = [ x if x in gussed_letters else '-' for x in word]
        print("lives = ", lives)
        print("word  = ", " ".join(curr_word), "\n")

        guess = input("guess your letter = ").upper()
        
        while len(guess) != 1:
            print("\nInvalid input!\n")
            guess = input("guess your letter = ").upper()    

        if guess in gussed_letters :
            print("Already guessed this letter, try another letter\n")
        elif guess in letters :
            print(f"Good guess, Letter {guess} is in the word\n")
            gussed_letters.append(guess)
        else :
            lives -= 1
            print("Inccorect guess!\n")

    if( lives == 0 ):
        print(f"Better luck! Next time. Word was \"{word}\".\n")
    else :
        print("Well Played, You guessed the word!\n")


if __name__ == '__main__':
    hangman()
