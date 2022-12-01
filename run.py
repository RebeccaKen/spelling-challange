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
This function will welcome the player.
Then it will collect their name as an input.
"""

def get_name():
    response = input('Welcome to hangman. Please enter your name:')
    return response

name = get_name()


if name.isalpha():
    print(f"Hello {name} it's nice to meet you" + "!")
    print('Welcome to Hangman. Ready to swing?')
elif name.isdigit():
    print('Sorry, you can only to use letters only to spell your player name!')
else:
    print('You cannot use any special characters in player name.')


correct = []
incorrect = []
failCount = 12
lettersGuessed = " "
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
    wrongLetterCount = 0


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


while True:
    displayBoard(incorrect, correct, secretWord)
    
    # Let the player enter a letter. 
    guess = getGuess(incorrect + correct)
    
    if guess in secretWord:
        correct = correct + guess

# Check if the player has won.

    foundAllLetters = True
    for i in range(len(secretWord))
    if secretWord[i] not in correct:
        foundAllLetters = False
        break
    if foundAllLetters:
        print('Yes! The secret word is "'+ secretWord +'"! You have won!')
        gameIsDone = True
    else:
        incorrect = incorrect + guess

    
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



    
    

