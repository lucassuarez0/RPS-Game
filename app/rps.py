# Rock Paper Scissors Game (Command Line)

# 1. Imports at the top
import random

# 2. Constants or global variables
VALID_OPTIONS = ["rock", "paper", "scissors"]

# 3. Functions or classes

def determine_winner(u, c):
    """
    Determines the winner of a game of rock paper scissors.

    Params:
        u (str): the user's choice, one of "rock", "paper", "scissors"
        c (str): the computer's choice, one of "rock", "paper", "scissors"

    Returns:
        str: "TIE GAME", "USER WINS", or "COMPUTER WINS"
    """
    if u == c:
        return "TIE GAME"
    elif (u == "rock" and c == "scissors") \
        or (u == "paper" and c == "rock") \
        or (u == "scissors" and c == "paper"):
        return "USER WINS"
    else:
        return "COMPUTER WINS"


# 4. Main conditional
if __name__ == "__main__":
    # Only run the code below if we execute this file from the command line,
    # but not if we import from this file.

    # ASK USER FOR AN INPUT (R/P/S)
    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    # VALIDATIONS
    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        quit()

    # GENERATE RANDOM COMPUTER CHOICE
    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    # DETERMINE THE WINNER
    result = determine_winner(u=user_choice, c=computer_choice)
    print(result)