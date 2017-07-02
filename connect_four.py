# functions: make_move, display, check_for_win
import os
from collections import namedtuple

columns = 7
rows = 6
Spot = namedtuple

turn_player1 = True
playing = True


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_turn():
    if turn_player1 == True:
        return "1"
    else:
        return "2"


def display():
    clear()
    print("Player {}'s Turn\n".format(get_turn()))
    print("1 2 3 4 5 6 7")
    for row in range(rows):
        for column in range(columns):
            pass


def get_input():
    # just need to ask for the column
    #import pdb; pdb.set_trace()
    while True:
        try:
            player_input = input("> ")
            if player_input == "Q":
                return "Q"
            else:
                column = int(player_input)
        except ValueError:
            print("Input must be a number")
            continue
        else:
            if column < 1 or column > columns:
                print("Column out of range")
                continue
            else:
                # the input is valid
                return column


def intro():
    clear()
    print("Welcome to Connect 4!")
    print("Type 'Q' at anytime to quit\n")
    input("Press any key to play")  
     
               
def game():
    intro()
    while playing == True:
        display()
        player_input = get_input()
        if player_input == 'Q':
            break

game()










