import random

#giving users options and taking input
user_action = input("Enter a choice(rock, paper, scissors): ")

#storing all possible options in a list
possible_actions = ["rock", "paper", "scissors"]

#using random function to choose a random
#choice from all three for computer
computer_action = random.choice(possible_actions)

#printing user and computer"s choice
print(f"\n You chose {user_action}, computer chose {computer_action}. \n")

#using if statement to compare
#and generate who is winner
if user_action == computer_action:
    print(f"Both players selected the {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cut paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
elif user_action == "paper":
    if computer_action == "scissors":
        print("Scissors cut Paper. You lose.")
    else:
        print("Paper covers Rocks! You win.")
