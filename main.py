from art import *
import random

game_images = [rock, paper, scissors]

game_on = True
def game():
    user_choice = int(input("What did you choose Type 0 for ROCK , 1 for PAPER , 2 for SCISSORS.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an incorrect number,YOU LOSE!!!")
    else:
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print(f"Computer chooses : ")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("YOU WIN!!!")
        elif computer_choice > user_choice:
            print("YOU LOSE!!!")
        elif computer_choice < user_choice:
            print("YOU WIN !!!")
        elif computer_choice == 0 and user_choice == 2:
            print("YOU LOSE!!!")
        elif computer_choice == user_choice:
            print("IT'S DRAW !!!")




while game_on:
    game()

    restart = input("Do you want to continue ? Y/N :").lower()
    if restart == 'y':
        game()
        restart = input("Do you want to continue ? Y/N :").lower()
    else :
        game_on = False

