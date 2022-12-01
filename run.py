import random

# f = open("list.txt", "r")
# secretWord = random.choice(words)
with open("list.txt", "r") as new_list:
    words = [item.replace("\n", "") for item in new_list.readlines()]

secretWord = random.choice(words)

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
This function will collect the player's age.
It then validates their input.

"""



while True:
    try:
        num = int(input("Please enter your age: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if num >= 8 and num <= 11:
        print(f'You entered: {num}')
        break
    else:
        print('This game is recommended for children of 8+!')

"""

"""

def get_player_name():
    name = input('Welcome to Hangman. Please enter your player name:' )
    return name 

player_name = get_player_name






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


    
    

    
    

