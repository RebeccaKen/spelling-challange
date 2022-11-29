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


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord =  random.choice(words).upper()
gameIsDone = False

# Welcome messages
name = input ('Welcome to Hangman. Please enter your player name:' )
if name.isalpha():
        print("Hello " + name + " it's nice to meet you" + "!")
        print('Welcome to Hangman. Ready to swing?')
        guess = input('Guess a letter: ')
elif name.isdigit():
        print('Sorry, you can only to use letters only to spell your player name! Try again')
else:
    print('You cannot use any special characters in player name.')


def play_game():
    """
    This function asks the player if they would like to play another game of hangman
    """
    reply = input('Would you like to play another game of hangman? Hit Y for Yes and N for No').upper()
if reply == 'Y':
    game_run()
else:
     print('Please play with us again soon')

def playerBoard(missedLetters, correctLetters, words):
    print(hangman_images[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')

    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(words)

    # Replace blanks with correctly guessed letters.

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            print('Right!')

    # Show the answer with spaces in between each letter.

    for letter in blanks: 
        print(letter, end=' ')
        print()

def getGuess(alreadyGuessed):
    while True: 
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Just the one letter, please')
        elif guess == guess.isalpha():
            print('Your guess must be a letter')
        elif guess == '_':
            print('You must enter a letter')
        elif guess == alreadyGuessed:
            print('You have already selected this letter. Try another letter!')
        else:
            return guess   


while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Let the player enter a letter.
guess = getGuess(missedLetters + correctLetters)
if guess in secretWord:
    correctLetters = correctLetters + guess
    
    # Check if the player has won. 
foundAllLetters = True
for i in range(len(secretWord)):
    if secretWord[i] not in correctLetters:
        foundAllLetters = False
    break
if foundAllLetters:
    print('Yes! The secret word is "' + secretWord +'"! You have won!')
    gameIsDone = True
else:
    missedLetters = missedLetters + guess


# Check if player has guessed too many times and lost.
if len(missedLetters) == len(HANGMAN_PICS) - 1:
    displayBoard(missedLetters, correctLetters, secretWord)
print('You have run out of guesses!\nAfter ' +
str(len(missedLetters)) + ' missed guesses and ' +
str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
gameIsDone = True

