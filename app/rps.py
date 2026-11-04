# Rock Paper Scissors Game (Command Line)

#Organisational structure of our python file

#1. Imports at the top
import random

#2. Constants or global variables
VALID_OPTIONS = ["rock", "paper", "scissors"]

#3. Functions or classes


#4. Main condiitonal
if __name__ == "__main__":
    #Only run the code below if we execute this file from the command line but not if we import from this file. 
    # ASK USER FOR AN INPUT (R/P/S)

    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    # VALIDATIONS

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        # exit()
        quit()

    # GENERATE RANDOM COMPUTER CHOICE

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    # DETERMINE THE WINNER

    # quick alias to facilitate some copy and pasting
    # we will soon move this into a function anyway
    u = user_choice
    c = computer_choice

    if u == "rock" and c == "rock":
        print("TIE GAME")
    elif u == "rock" and c == "paper":
        print("COMPUTER WINS")
    elif u == "rock" and c == "scissors":
        print("USER WINS")
    elif u == "paper" and c == "rock":
        print("COMPUTER WINS") # OOPS
    elif u == "paper" and c == "paper":
        print("TIE GAME")
    elif u == "paper" and c == "scissors":
        print("USER WINS") # OOPS
    elif u == "scissors" and c == "rock":
        print("COMPUTER WINS")
    elif u == "scissors" and c == "paper":
        print("USER WINS")
    elif u == "scissors" and c == "scissors":
        print("TIE GAME")