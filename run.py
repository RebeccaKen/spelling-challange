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

list = ['enjoy', 'honey', 'hapless', 'groan', 'statement', 'teeny', 'physical', 'wretched', 'turkey', 'trains', 'fly', 'straps']
secretWord = random.choice(list)


# Welcome messages
name = input ('Welcome to Hangman. Please enter your player name:' )
if name.isalpha():
    print("Hello " + name + " it's nice to meet you" + "!")
    print('Welcome to Hangman. Ready to swing?')
elif name.isdigit():
    print('Sorry, you can only to use letters only to spell your player name! Try again')
else:
    print('You cannot use any special characters in player name.')

correct = []
incorrect = []
failCount = 6

while True:

    print('===============================')

    guess = input('Please enter a letter:')

    if guess in secretWord:
        correct.append(guess)
        print('Correct')
    else:
        failCount -= 1
        incorrect.append(guess)
        print('Incorrect')
    


