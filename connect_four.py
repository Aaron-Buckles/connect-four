# functions: make_move, check_for_win
import os

columns = 7
rows = 6

turn_player1 = True
rows_list = []
empty = 'O'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_spots():
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(empty)
        rows_list.append(row)


def get_turn():
    if turn_player1 == True:
        return "1"
    else:
        return "2"


def display():
    clear()
    print("Player {}'s Turn\n".format(get_turn()))
    print("1 2 3 4 5 6 7")
    print("-------------")
    for row in range(rows):
        for column in range(columns):
            print(rows_list[row][column], end=' ')
            if column == columns-1:
                print("", end='\n')


def get_input():
    # just need to ask for the column
    while True:
        try:
            player_input = input("\n> ")
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


def make_move(column):
    # the piece must go down as far as possible
    row = -1
    new_column = column
    
    while True:          
        if row >= -rows or new_column != column:
            if new_column != column:
                column = new_column
                row = -1
            if rows_list[row][column-1] == empty:
                # fill the spot with the player's number
                rows_list[row][column-1] = get_turn()
                # next player's turn
                global turn_player1 
                turn_player1 = not turn_player1
                break
            else:
                # stack the pieces on one another
                row -= 1
        else:
            print("Row out of range")
            new_column = get_input()


def intro():
    clear()
    print("Welcome to Connect 4!")
    print("Type 'Q' at anytime to quit\n")
    input("Press any key to play")  
     
               
def game():
    init_spots()
    intro()
    # the game loop
    while True:
        display()
        player_input = get_input()
        if player_input == 'Q':
            break
        make_move(player_input)


game()










