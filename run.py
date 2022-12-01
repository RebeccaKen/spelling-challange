import random


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



"""

""" 

words = ['domination', 'leadership', 'foundation', 'experience', 'hemisphere', 'reputation', 'indication', 'occupation', 'innovation', 'wilderness']
secretWord = random.choice(words)





"""
This function will collect the player's name.
It will then validate their input.
"""
while True:
    try:
        num = int(input("Enter you age: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if num >= 1 and num <= 10:
        print(f'You entered: {num}')
        break
    else:
        print('You must be between one and ten')


correct = []
incorrect = []
failCount = 10
lettersGuessed = " "


while failCount > 0:

    print('===============================')

    guess = input('Please enter a letter:')

    if guess in secretWord:
        correct.append(guess)
        print(f"Correct! There is one or more {guess} in the secretWord")
    else:
        failCount -= 1
        incorrect.append(guess)
        print(f"Incorrect! There is no {guess} in the answer.")
    
    lettersGuessed = lettersGuessed + guess




    def displayBoard(hangman_images, incorrect, correct, secretWord):
        print(hangman_images[len(incorrect)])
    print()

    print('Missed Letters:', end=' ')
    for letter in incorrect:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correct:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


    
    

    
    

