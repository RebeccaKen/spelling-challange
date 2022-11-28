import random

# Constants

hangman_images = ['''
    +---+    
    |   |
        |
        |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
        |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
    |   |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|   |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|\  |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|\  |
   /    |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
===========''']

words = ['ENJOY', 'HONEY', 'HAPLESS', 'GROAN', 'STATEMENT', 'TEENY', 'PHYSICAL', 'WRETCHED', 'TURKEY', 'TRAINS', 'FLY', 'STRAPS']

plays_remaining = 11


# Function to generate a random word

def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]

    answer = pick_a_word()

# Welcome message

print('Welcome to Hangman. Ready to swing?')

guess = input('Guess a letter: ').upper()

"""
This function will construct a display board for the user
"""
def displayBoard(missedLetters, correctLetters, answer):
    print(hangman_images[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')

    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(answer)

    # Replace blanks with correctly guessed letters.

    for i in range(len(answer)): 
        if answer[i] in correctLetters:
            blanks = blanks[:i] + answer[i] + blanks[i+1:]
            print('Right!')

    # Show the answer with spaces in between each letter.

    for letter in blanks: 
        print(letter, end=' ')
print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
        while True:
             guess = input()
             guess = guess.upper()
             if len(guess) != 1:
                 print('Please enter a single letter.')
                 elif guess in alreadyGuessed:
                     print('You already entered that letter. Pick another letter')
