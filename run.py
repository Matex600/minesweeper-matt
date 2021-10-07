import random
import os
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("--------- Welcome to Minesweeper ---------")
print(" --------- --------- --------- ---------")
print("------ Start by entering username! ------")

username = input()

print("----- Welcome, " + username + ", good luck & have fun! -----\n")
print('''Game instruction! \n
         1. Enter a number between 1 and 8 for row
            and column. (Example: 3, hit enter and 5)\n''')
def initialize_game_board():
    """
    Function defines global variables and
    creates the game board using the value j
    for columns and rows through the use of for loops
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


# def player_input():


# def game_over():



def main():
    initialize_game_board()
    

main()

