import os
import sys

from win_combinations import WIN_COMBOS

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
                sys.exit()
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
                break
            else:
                # stack the pieces on one another
                row -= 1
        else:
            print("Row out of range")
            new_column = get_input()


def get_all_spots():
    # use rows_list to generate a list of all spots on the board
    all_spots = []
    for row in rows_list:
        for column in row:
            all_spots.append(column)
    return all_spots


def check_combination(combo):
    #print(combo)
    for WIN_COMBO in WIN_COMBOS:
        for index, spot in enumerate(combo):
            if spot == 'X':
                continue
            if WIN_COMBO[index] != spot:
                # break if there is a difference between combos
                break
        else:
            # this occurs if the combos match exactly
            display()
            print("Player {} Wins!".format(get_turn()))
            sys.exit()
            

def check_for_win():
    # must convert CURRENT player's symbol (1 or 2) into a X
    #print("All: " + str(get_all_spots()))
    all_spots = []
    for spot in get_all_spots():
        if spot == get_turn():
            all_spots.append('X')
        else:
            all_spots.append('O')
    #print("New: " + str(all_spots))
    #print("Rows List: " + str(rows_list))
    # now check all 4 x 4 areas
    size = 4
    for row in range((rows+1) - size):
        # if row == 1:
        #     import pdb; pdb.set_trace()
        for column in range((columns+1) - size):
            # create a 4 x 4 combo
            combo = []
            for row_offset in range(size):
                for col_offset in range(size):
                    # index = x + width * y
                    final_row = row + row_offset
                    final_col = column + col_offset
                    index = final_col + (columns * final_row)
                    combo.append(all_spots[index])
            check_combination(combo)


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
        make_move(player_input)
        check_for_win()
        # next player's turn
        global turn_player1 
        turn_player1 = not turn_player1


game()










