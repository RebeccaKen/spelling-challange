def main():
    """
    Define main as a function to incase the rest of Spelling Challange code
    """

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

    while True:
        try:
            num = int(input("Enter you age: "))
            if num < 8:
                print("This game may be a bit too hard for you.")
            elif num > 11:
                print("This game may be too easy for you")
            else:
                print('This game is recommended for children of 8+!')
                break

        except ValueError:
            print("Please enter a number")

    correct = []
    incorrect = []
    game_done = True
    fail_count = 0
    letters_guessed = ' '
    guess = ' '

    # The following while loop code was created using the tutorial
    # 'How to Build a Hangman Game with Python' by CBT Nuggets.

    while fail_count < 10:

        print("===============================")

        guess = input("Please enter a letter:\n")

        if guess in secretWord:
            correct.append(guess)
            print(f"Correct! There is a {guess}")
        if guess not in secretWord:
            incorrect.append(guess)
            print(f"Incorrect! There is no {guess} in the answer.")
            fail_count += 1

        letters_guessed += guess

        test_answer = [x for x in secretWord if x in correct]
        print(test_answer, "test answer")

        for letter in secretWord:
            if letter in letters_guessed:
                print(f"{letter}", end=" ")
            if letter not in letters_guessed:
                print("_", end=" ")
    # Check if player's guesses are all correct.
        if len(test_answer) == len(secretWord):
            print(f"You won! The answer was {secretWord}")
            print("=====================================")
            game_done = True
            break
        elif fail_count == 10:
            print(f"You've run out of guesses. Answer = {secretWord}")
            print("===================================================")
            game_done = True
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
