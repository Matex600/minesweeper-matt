import random
import os
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("--------- Welcome to Minesweeper ---------")
print(" --------- --------- --------- ---------")
print("------ Start by entering username! ------")

username = input()

print("----- Welcome, " + username + ", good luck & have fun! -----\n")
mine_values = 8
j = 8

def initialize_game_board():
    """
    Create game board using columns and rows
    """
    print("    Game started ... \n")
    global mine_values
    global j
    

    print()
    
    cell_block = "   "
    for i in range(j):
        cell_block = cell_block + "     " + str(i + 1)
    print(cell_block)

    for r in range(j):
        cell_block = "     "
        if r == 0:
            for col in range(j):
                cell_block = cell_block + "______"  
            print(cell_block)

        cell_block = "     "
        for col in range(j):
            cell_block = cell_block + "|     "
        print(cell_block + "|")

        cell_block = "  " + str(r + 1) + "  "
        for col in range(j):
            cell_block = cell_block + "|  " + str(mine_values[r][col]) + "  "
        print(cell_block + "|")

        cell_block = "     "
        for col in range(j):
            cell_block = cell_block + "|_____"
        print(cell_block + "|")  

    print()

# def inject_bombs(bombs):
    # """
    # inject randomised bombs to game board
    # """
    # for

# def player_input():
"""
"""


# def game_over():
"""
"""


def main():
    initialize_game_board()
    

main()

