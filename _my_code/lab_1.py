# Richard Farr
# December 11th, 2020
# PDX Code Guild
# Programming 102
# Lab 1


"""
    Title: Rock, Paper, Scissors
    Description: Let's play rock, paper scissors
    Author: Anthony
"""
import random  # We need to import random before we can use it


# These are the available choices, we can use this for both the user and computer
choices = ["rock", "paper", "scissors"]

# This is our main loop, It will continue to run our game until we break out of it
while True:
    # Printing a welcome message everytime our game loops
    print(" ") # add another empty line so easier to read
    print("Welcome to Rock, Paper, Scissors. Type 'done' at any time to exit")

    # Choosing a random option from our choices for the computer
    computer = random.choice(choices)
    # print("") # add empty line so easier to read
    print("computer is: " + computer) # make the game easier to win

    user = ""
    # Continue looping while the user has not made a valid selection
    while user not in choices:
        user = input("Choose either 'rock', 'paper', or 'scissors'").lower()

        # if the user types done, we want to stop asking them
        if user == "done":
            break

    # if user equals done, we want to end the game
    if user == "done":
        break

    # if the user and computer are the same it is a tie
    if user == computer: # 1 - users to user
        print("Looks like a tie") # 2 add )

    # check all cases if user is rock
    elif user == "rock":

        # check winning case
        if computer == "scissors":
            print("You win!")

        # check losing case
        elif computer == "paper": # 3 change rock to paper
            print("Sorry, You lose.")

    # check all cases if user is paper
    elif user == "paper":

        # check winning case
        if computer == "rock": # 4 add :
            print("You win!")

        # check losing case
        elif computer == "scissors":
            print("Sorry, You lose.")

    # check all cases if user is scissors
    elif user == "scissors":

        # check winning case
        if computer == "paper":
            print("You win!")

        # check losing case
        elif computer == "rock":
            print("Sorry, You lose.") # 5 P to p on print