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

    # validation method will be used to assure the player's name uses letters
    if name.isalpha():
        print(f"Hello {name} it's nice to meet you" + "!")
        print("Ready to go?")
    elif name.isdigit():
        print("Please use letters!")
    else:
        print("You cannot use any special characters in player name.")
        
    # This try/except statement will collect the player's age.
    # It then validates their input.
    # If the player is not between 8-11 a message
    # will appear to clarify the recommended player age.

    correct = []
    incorrect = []
    game_Done = True
    fail_Count = 0
    letterGuessed = ' '
    secretWord = random.choice(words)
    guess = ' '

    # The following while loop code was created using the tutorial
    # 'How to Build a Hangman Game with Python' by CBT Nuggets.
    
    while fail_Count > 0:

        print("===============================")

        guess = input("Please enter a letter:\n")

        if guess in secretWord:
            correct.append(guess)
            print(f"Correct! There is a {guess}")
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
            else:
                print(f"You've run out of guesses. Answer = {secretWord}")
                print("===================================================")
                game_Done = True
                break


        # Restart game if user chooses to do so using main()
        restart = input("Start again? y for Yes, n for No:\n")
        if restart == ("y"):
           incorrect = []
           correct = []
           main()
        else:
            quit()

main()
