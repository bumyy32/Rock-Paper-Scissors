# This is my rock, paper, scissors game!
import random
from colorama import *

playing = True

# Rounds
rounds_played = 0
player_win = 0
opponent_win = 0

while playing:
    # Rounds played:
    print(Fore.YELLOW + f"This is the round {rounds_played}!\n"
                        f"Player: {player_win} / Opponent:{opponent_win}")
    # Player input
    user_action = input(Fore.CYAN + "Please, choose among rock, paper and scissor: ")

    # Computer Input
    print(Fore.LIGHTMAGENTA_EX + "\nYour opponent is thinking...")
    computer_answers = ['rock', 'paper', 'scissor']
    computer_action = random.choice(computer_answers)

    # Showing the choices:
    print(f"You choose {user_action}, and your opponent choose {computer_action}\n")

    if user_action == computer_action:
        print(f"Both player choose {user_action}, it's a tie!")
    elif user_action.lower() == 'rock':
        if computer_action == 'scissor':
            print("Rock breaks scissors! You won!")
            player_win += 1
        else:
            print("Paper wraps rock! You lost!")
            opponent_win += 1
    elif user_action.lower() == 'paper':
        if computer_action == 'scissor':
            print("Scissor cuts paper! You lost!")
            opponent_win += 1
        else:
            print("Paper wraps rock! You won!")
            player_win += 1
    elif user_action.lower() == 'scissor':
        if computer_action == 'paper':
            print("Scissor cuts paper! You won!")
            player_win += 1
        else:
            print("Rock breaks scissors! You lost!")
            opponent_win += 1

    play_again = input(Fore.YELLOW + "\nDo you want to play again? (yes / no): ")

    if play_again.lower() == 'yes':
        playing = True
        rounds_played += 1

    elif play_again.lower() == 'no':
        print("Well, cya!")
        playing = False
        break
    else:
        print("Please, try again!")

# Main check
if __name__ == '__main__':
    pass
