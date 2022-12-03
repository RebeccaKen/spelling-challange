import random

# Code to connect run.py to word list in list.txt
with open("list.txt", "r") as new_list:
    words = [item.replace("\n", "") for item in new_list.readlines()]

secretWord = random.choice(words)


"""
This try/except statement will collect the player's age.
It then validates their input.
If the player is not between 8-11 a message will appear to 
clarify the recommended player age.

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
        print('This game is recommended for children age 8 - 11!')


def get_name():
    '''This Function to welcome the player and collect their name as an input.'''
    response = input('Welcome to hangman. Please enter your name:')
    return response


name = get_name()


# This input validation method will be used to assure the player's name is in letters

if name.isalpha():
    print(f"Hello {name} it's nice to meet you" + "!")
    print('Welcome to Spelling Challange. Ready to go?')
elif name.isdigit():
    print('Sorry, you can only to use letters only to spell your player name!')
else:
    print('You cannot use any special characters in player name.')


correct = []
incorrect = []
failCount = 12
lettersGuessed = ""
gameIsDone = False

#The playAgain function could was built using '8 - Writing Hangman code' on www.inventwithpython.com

def playAgain():
    """This function returns True if the player wants to play again;otherwise, it returns False."""
    print('Do you want to play Spelling Challange again? (yes or no)')
    return input().lower().startswith('y')

"""
The following code was created using the tutorial 
'How to Build a Hangman Game with Python' by CBT Nuggets.
"""


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
    failCount = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            failCount += 1

    print(correct)
    if len(correct) == len(secretWord):
        gameIsDone = True
        print('You won!')
    
    # Check if player has guessed too many times and lost.
    if len(incorrect) == len(secretWord) - 1:
        print(f"You've run out of guesses. The answer was {secretWord}")
        gameIsDone = True
        
    # Ask the player if they want to play again (but only if the game is done).

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
        else:
            print("we are here")

    




