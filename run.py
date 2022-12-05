def main():

    import random

    # Code to connect run.py to word list in list.txt for use in secretWord
    with open("list.txt", "r") as new_list:
        words = [item.replace("\n", "") for item in new_list.readlines()]

    secretWord = random.choice(words)

    def get_Name():
        '''This welcome Function collects player's name as an input.'''
        response = input("Welcome to Spelling Challange! Enter your name:\n")
        return response

    name = get_Name()

    """
    This try/except statement will collect the player's age.
    It then validates their input.
    If the player is not between 8-11 a message
    will appear to clarify the recommended player age.
    """

    while True:
        try:
            num = int(input("Please enter your age:\n"))
        except ValueError:
            print("Please enter a valid number")
            continue
        if num >= 8 and num <= 11:
            print(f'You entered: {num}')
            break
        else:
            print("This game is recommended for children age 8 - 11!")

    # validation method will be used to assure the player's name uses letters
    if name.isalpha():
        print(f"Hello {name} it's nice to meet you" + "!")
        print("Ready to go?")
    elif name.isdigit():
        print("Sorry, you can only to use letters!")
    else:
        print("You cannot use any special characters in player name.")

    correct = []
    incorrect = []
    fail_Count = 7
    letters_Guessed = " "
    game_Done = True

    # The following code was created using the tutorial
    # 'How to Build a Hangman Game with Python' by CBT Nuggets.

    while fail_Count > 0:

        print("===============================")

        guess = input("Please enter a letter:")

        if guess in secretWord:
            correct.append(guess)
            print(f"Correct! There is one or more {guess} in the answer")
            fail_Count -= 1
        else:
            incorrect.append(guess)
            print(f"Incorrect! There is no {guess} in the answer.")

        letters_Guessed = letters_Guessed + guess
        fail_Count = 0

        for letter in secretWord:
            if letter in letters_Guessed:
                print(f"{letter}", end=" ")
            if letter not in letters_Guessed:
                print("_", end=" ")
                fail_Count += 1

            # Check if player's guesses are all correct.
            if len(correct) == len(secretWord):
                print(f"You won! The answer was {secretWord}")
                print("=====================================")
                game_Done = True
                break
            # Check if player has guessed too many times and lost.
            if len(incorrect) == len(secretWord) - 1:
                print(f"You've run out of guesses. Answer = {secretWord}")
                print("===================================================")
                game_Done = True
                break

    # Restart game if user chooses to do so using main()
    restart = input("Start again? y for Yes, n for NO:\n")
    if restart == ("y"):
        incorrect = []
        incorrect = []
        main()
    else:
        quit()


main()
