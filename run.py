import random

# f = open("list.txt", "r")
# secretWord = random.choice(words)
with open("list.txt", "r") as new_list:
    words = [item.replace("\n", "") for item in new_list.readlines()]

secretWord = random.choice(words)


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
This function will welcome the player.
Then it will collect their name as an input.
"""

def get_name():
    response = input('Welcome to hangman. Please enter your name:')
    return response

name = get_name()

# This input validation method will be used to assure the player's name is in letters

if name.isalpha():
    print(f"Hello {name} it's nice to meet you" + "!")
    print('Welcome to Hangman. Ready to swing?')
elif name.isdigit():
    print('Sorry, you can only to use letters only to spell your player name!')
else:
    print('You cannot use any special characters in player name.')


correct = []
incorrect = []
failCount = 6
lettersGuessed = ""
run_game = " "
gameOver = False

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

    if failCount == 0:
        print(f"Congrats! The answer was {secretWord}")
        break

else:
    print("Sorry! Maybe next time you will win!")






    
def playGame():
    global runGame
    playGame = input("Do You want to play again? y = yes, n = no \n")
    while playGame not in ["y", "n","Y","N"]:
        playGame = input("Do You want to play again? y = yes, n = no \n")
    if playGame == "y":
        main()
    elif playGame == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()



    
    

