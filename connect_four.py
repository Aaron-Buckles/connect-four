# functions: make_move, display, check_for_win
import os

columns = 7
rows = 6

turn_player1 = True


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display():
    clear()


def get_input():
    # just need to ask for the column
    while True:
        try:
            column = int(input("> "))
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
    print("")
    input("Press any key to play")
    clear()  
     
               
def game():
    intro()
    # game loop can go here


game()










