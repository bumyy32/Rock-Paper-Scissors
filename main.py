# This is my rock, paper, scissors game!
import random
from colorama import *

playing = True

while playing:
    # Player input
    user_action = input(Fore.CYAN + "Please, choose among rock, paper and scissor: ")

    # Computer Input
    print(Fore.LIGHTMAGENTA_EX + "Your opponent is thinking...")
    computer_answers = ['rock', 'paper', 'scissor']
    computer_action = random.choice(computer_answers)

    # Showing the choices:
    print(f"You choose {user_action}, and your opponent choose {computer_action}")

    if user_action == computer_action:
        print(f"Both player choose {user_action}, it's a tie!")
    elif user_action.lower() == 'rock':
        if computer_action == 'scissor':
            print("Rock breaks scissors! You won!")
        else:
            print("Paper wraps rock! You lost!")
    elif user_action.lower() == 'paper':
        if computer_action == 'scissor':
            print("Scissor cuts paper! You lost!")
        else:
            print("Paper wraps rock! You won!")
    elif user_action.lower() == 'scissor':
        if computer_action == 'paper':
            print("Scissor cuts paper! You won!")
        else:
            print("Rock breaks scissors! You lost!")

    play_again = input(Fore.YELLOW + "Do you want to play again? (yes / no): ")

    if play_again.lower() == 'yes':
        playing = True
    elif play_again.lower() == 'no':
        print("Well, cya!")
        playing = False
        break
    else:
        print("Please, try again!")

# Main check
if __name__ == '__main__':
    pass
