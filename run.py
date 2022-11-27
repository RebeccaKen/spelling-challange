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

guessed_letters = '-'

wrong_guesses = 0

used_letters = []

# Function to generate a random word

def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]
