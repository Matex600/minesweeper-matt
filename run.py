import random
import os
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
global j
global mine_values
global mine_amount
global numbers

# Welcome message and username prompt
print("--------- Welcome to Minesweeper ---------")
print(" --------- --------- --------- ---------")
print("------ Start by entering username! ------")

username = input()

# Message after username input with game instructions
print("----- Welcome, " + username + ", good luck & have fun! -----\n")
print('''Game instruction! \n
        1. Enter a number between 1 and 6 for row
            and column. (Example: 3, hit enter and 5)
        2. Hitting a mine results in game over\n''')


def initialize_game_board():
    """
    Function defines global variables and
    creates the game board using the value j
    for columns and rows through the use of for loops
    """
    print("    Game starting ... \n")
    j = 6
    mine_values = [[' ' for y in range(j)] for x in range(j)]
    print()
    
    # Layout of Minesweeper game area
    cell_block = "   "
    for i in range(j):
        cell_block = cell_block + "     " + str(i + 1)
    print(cell_block)

    # For loop creates squares in the grid using | and _
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


def inject_bombs():
    """
    This function stores data and values from the mines
    and flags
    """
    # Size of grid (6x6)
    j = 6
    # Number of mines present
    mine_amount = 4

    # Actual (hidden) values of the grid
    numbers = [[0 for y in range(j)] for x in range(j)]
    # Visible values of the grid
    mine_values = [[' ' for y in range(j)] for x in range(j)]

    # Flagged positions
    flag = []

    # Tracking umber of mines already set starts at 0
    mine_count = 0
    while mine_count < mine_amount:

        # Random number for grid positions
        grid_positions = random.randint(0, j*j -1)

        # Generate row and column from numbers in grid
        r = grid_positions // j
        col = grid_positions % j

        # Add a mine if there are none on the grid
        if numbers[r][col] != - 1:
            mine_count = mine_count + 1
            numbers[r][col] = - 1


def actual_board_values()
    """
    This function sets up board values that are hidden from
    the player and work in the background, checking the board for
    presence of mines using a for loop
    """
    # Loop that counts every cell in the grid
    for r in range(j):
        for col in range(j):
            
            # Skips check if a mine is present
            if numbers[r][col] == - 1
                continue

            # Checks input above
            if r > 0 and numbers[r-1][col] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks input below
            if r < j-1 and numbers[r+1][col] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks left input
            if col > 0 and numbers[r][col-1] == - 1:
                numbers[r][c] = numbers[r][c] + 1

            # Checks right input
            if col < j - 1 and numbers[r][col+1] == - 1
                numbers[r][col] = numbers[r][col] + 1

            # Checks top left input
            if r > 0 and col > 0 and numbers[r-1][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks top right input
            if r > 0 and col < j - 1 and numbers[r-1][col+1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks bottom left input
            if r < j - 1 and col > 0 and numbers[r+1][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks bottom right input
            if r < j - 1 and col < n - 1 and numbers[r + 1][col + 1] == - 1:
                numbers[r][col] = numbers[r][col] + 1   
                        


# def player_input():


# def game_over():


def main():
    initialize_game_board()
    inject_bombs()
    

main()

