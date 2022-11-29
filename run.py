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

def pick_a_word():
    """
    This function will generate a word that the user will try to guess
    
    """
    words = ['ENJOY', 'HONEY', 'HAPLESS', 'GROAN', 'STATEMENT', 'TEENY', 'PHYSICAL', 'WRETCHED', 'TURKEY', 'TRAINS', 'FLY', 'STRAPS']
    return random.choice(words).upper()

# Welcome messages
name = input ('Welcome to Hangman. Please enter your player name:' )
if name.isalpha():
        print("Hello " + name + " it's nice to meet you" + "!")
        print('Welcome to Hangman. Ready to swing?')
        guess = input('Guess a letter: ')
elif name.isdigit():
        print('Sorry, you can only to use letters only to spell your player name!')
else:
    print('You cannot use any special characters in player name.')

 
def displayBoard(missedLetters, correctLetters, words):
    print(hangman_images[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')

    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(words)

    # Replace blanks with correctly guessed letters.

    for i in range(len(words)): 
        if words[i] in correctLetters:
            blanks = blanks[:i] + words[i] + blanks[i+1:]
            print('Right!')

    # Show the answer with spaces in between each letter.

    for letter in blanks: 
        print(letter, end=' ')
        print()

