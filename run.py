"""
Imported modules     describe file briefly.
"""
import random
import os
import time
import sys

# Welcome message and username prompt
def enter_username():
    """
    Function for username input
    """
    print("--------- Welcome to Minesweeper ---------")
    print(" --------- --------- --------- ---------")
    print("------ Start by entering username! ------")
    username = input(" \n")
    print("----- Welcome, " + username + ", good luck & have fun! -----\n")
    return username


# Message after username input with game instructions
def instructions():
    """
    Game instruction function
    """
    print('''Game instructions!
          1. Game size depends on difficulty
          2. Enter a number between 1 and 8 for row
          and column. (Example: '3 5' '3 5 F')
          3. Flag a mine by making a selection and adding 'F' 
          4. Hitting a mine results in game over!''')

    print("    Game loading ... \n")
    time.sleep(2)


def game_difficulty():
    """
    Function lets user decide game difficulty
    """
    print("Select game difficulty!")
    while True:
        game_difficulty_input = input(
                  "Enter 4 for Easy"
                  " 6 for Standard"
                  " 8 for Hard \n")
        try:
            if (int(game_difficulty_input) not in [4, 6, 8]):
                raise ValueError
            else:
                if int(game_difficulty_input) == 4:
                    print("You have chosen Easy difficulty")
                elif int(game_difficulty_input) == 6:
                    print("You have chosen Standard difficulty")
                elif int(game_difficulty_input) == 8:
                    print("You have chosen Hard difficulty")
                time.sleep(2)
                global GRID_SIZE
                GRID_SIZE = int(game_difficulty_input)
                global MAX_MINE_NUM
                MAX_MINE_NUM = int(game_difficulty_input)
                break
        except ValueError:
            print("Input is incorrect.. please make correct selection")
            time.sleep(2)


def initialize_game_board():
    """
    Function defines global variables and
    creates the game board using the value GRID_SIZE
    for columns and rows through the use of for loops
    """
    global MINE_VALUES
    global GRID_SIZE
    print()
    # Layout of Minesweeper game area
    cell_block = "   "
    for i in range(GRID_SIZE):
        cell_block = cell_block + "     " + str(i + 1)
    print(cell_block)

    # For loop creates squares in the grid using | and _
    for row in range(GRID_SIZE):
        cell_block = "     "
        if row == 0:
            for col in range(GRID_SIZE):
                cell_block = cell_block + "______"
            print(cell_block)

        cell_block = "     "
        for col in range(GRID_SIZE):
            cell_block = cell_block + "|     "
        print(cell_block + "|")

        cell_block = "  " + str(row + 1) + "  "
        for col in range(GRID_SIZE):
            cell_block = cell_block + "|  " + str(MINE_VALUES[row][col]) + "  "
        print(cell_block + "|")

        cell_block = "     "
        for col in range(GRID_SIZE):
            cell_block = cell_block + "|_____"
        print(cell_block + "|")

    print()


def inject_bombs():
    """
    This function stores data and values from the mines
    and flags
    """
    global NUMBERS
    global GRID_SIZE
    global MAX_MINE_NUM

    mine_count = 0

    while mine_count < MAX_MINE_NUM:

        # Random number for grid positions
        val = random.randint(0, GRID_SIZE*GRID_SIZE - 1)

        # Generate row and column from numbers in grid
        row = val // GRID_SIZE
        col = val % GRID_SIZE

        # Add a mine if there are none on the grid
        if NUMBERS[row][col] != - 1:
            mine_count = mine_count + 1
            NUMBERS[row][col] = - 1


def actual_board_values():
    """
    This function sets up board values that are hidden from
    the player and work in the background, checking the board for
    presence of mines using a for loop
    """
    global NUMBERS
    global GRID_SIZE

    # Loop that counts every cell in the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):

            # Skips check if a mine is present
            if NUMBERS[row][col] == - 1:
                continue

            # Checks input above
            if row > 0 and NUMBERS[row-1][col] == - 1:
                NUMBERS[row][col] = NUMBERS[row][col] + 1

            # Checks input below
            if row < GRID_SIZE-1 and NUMBERS[row+1][col] == - 1:
                NUMBERS[row][col] = NUMBERS[row][col] + 1

            # Checks left input
            if col > 0 and NUMBERS[row][col-1] == - 1:
                NUMBERS[row][col] = NUMBERS[row][col] + 1

            # Checks right input
            if col < GRID_SIZE - 1 and NUMBERS[row][col+1] == - 1:
                NUMBERS[row][col] = NUMBERS[row][col] + 1

            # Checks top left input
            if row > 0 and col > 0 and NUMBERS[row-1][col-1] == - 1:
                NUMBERS[row][col] = NUMBERS[row][col] + 1

            # Checks top right input
            if (row > 0 and
                col < GRID_SIZE - 1 and
                    NUMBERS[row-1][col+1] == - 1):
                NUMBERS[row][col] = NUMBERS[row][col] + 1

            # Checks bottom left input
            if (row < GRID_SIZE - 1 and col > 0 and
                    NUMBERS[row+1][col-1] == - 1):
                NUMBERS[row][col] = NUMBERS[row][col] + 1

            # Checks bottom right input
            if (row < GRID_SIZE - 1 and
                col < GRID_SIZE - 1 and
                    NUMBERS[row+1][col+1] == -1):
                NUMBERS[row][col] = NUMBERS[row][col] + 1


def terminate_game():
    """
    Function that allows user to restart game
    or terminate application
    """

    while True:
        try:
            terminate_game_input = int(
                input("Enter 1 to play again or 2 to terminate game \n"))
            if terminate_game_input == 1:
                print("Ready to try again?")
                time.sleep(2)
                main()
            if terminate_game_input == 2:
                print("Thank you for playing")
                time.sleep(2)
                clear()
                sys.exit()
        except ValueError:
            print("This is an incorrect input.. please try again!")
            terminate_game_input()


def adjoining_cells(row, col):
    """
    This is a recursive function to display all empty cells
    marked with (0)
    """
    global MINE_VALUES
    global NUMBERS
    global EMPTY_CELL

    # If cell is empty
    if [row, col] not in EMPTY_CELL:

        # Mark visited cell
        EMPTY_CELL.append([row, col])

        # 0 value cell
        if NUMBERS[row][col] == 0:
            MINE_VALUES[row][col] = NUMBERS[row][col]

            if row > 0:
                adjoining_cells(row-1, col)
            if row < GRID_SIZE-1:
                adjoining_cells(row+1, col)
            if col > 0:
                adjoining_cells(row, col-1)
            if col < GRID_SIZE-1:
                adjoining_cells(row, col+1)
            if row > 0 and col > 0:
                adjoining_cells(row-1, col-1)
            if row > 0 and col < GRID_SIZE-1:
                adjoining_cells(row-1, col+1)
            if row < GRID_SIZE-1 and col > 0:
                adjoining_cells(row+1, col-1)
            if row < GRID_SIZE-1 and col < GRID_SIZE-1:
                adjoining_cells(row+1, col+1)
        # If not empty cell
        if NUMBERS[row][col] != 0:
            MINE_VALUES[row][col] = NUMBERS[row][col]


def clear():
    """
    This function clears the terminal
    """
    os.system("clear")


def display_mines():
    """
    Displays mines to player once a square in the grid
    with a mine present
    """

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if NUMBERS[row][col] == - 1:
                MINE_VALUES[row][col] = 'M'


def check_game_concluded():
    """
    Function to check if game has conculded
    """
    global MINE_VALUES
    global GRID_SIZE
    global MAX_MINE_NUM

    mine_count = 0
    # Loop to check each square in grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # If the cell contains mine
            if MINE_VALUES[row][col] != ' ' and MINE_VALUES[row][col] != 'F':
                mine_count = mine_count + 1

    if mine_count == GRID_SIZE * GRID_SIZE - MAX_MINE_NUM:
        return True
    else:
        return False


def main():
    """
    Main function that runs the game
    from start to end
    """
    global GRID_SIZE
    global MAX_MINE_NUM
    global NUMBERS
    global EMPTY_CELL
    global MINE_VALUES

    # Grid Values
    GRID_SIZE = 8
    MAX_MINE_NUM = 8
    NUMBERS = [[0 for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]
    MINE_VALUES = [[' ' for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]
    flags = []

    enter_username()
    game_difficulty()
    instructions()
    inject_bombs()
    actual_board_values()

    # This variable maintains the game loop
    over = False
    # Game loop
    while not over:
        """
        While loop handles grid cells that have
        already been selected or not
        if it is already displayed to user and checks
        that number of flags does not exceed number of mines
        """
        initialize_game_board()

        player_input = input("Enter a row and column number = \n").split()

        # Standard player input check
        if len(player_input) == 2:
            try:
                val = list(map(int, player_input))
                print("Input selected: ", player_input)
                time.sleep(1)
            except ValueError:
                print("Input is incorrect.. please make correct selection")
                time.sleep(2)
                instructions()
                continue
        # Flag input check
        elif len(player_input) == 3:
            if player_input[2] != 'F' and player_input[2] != 'f':
                print("Incorrect input.. try again")
                time.sleep(2)
                instructions()
                continue
            try:
                val = list(map(int, player_input[:2]))
            except ValueError:
                print("Incorrect input.. try again")
                time.sleep(2)
                instructions()
                continue
            if (val[0] > GRID_SIZE or
                val[0] < 1 or
                    val[1] > GRID_SIZE or
                    val[1] < 1):
                print("Incorrect input.. try again")
                time.sleep(2)
                instructions()
                continue
            # Getting row and column numbers
            row = val[0]-1
            col = val[1]-1

            # If grid cell already flagged by user
            if [row, col] in flags:
                print("This cell has already been flagged")
                time.sleep(2)
                continue
            # If grid cell already displayed to user
            if MINE_VALUES[row][col] != ' ':
                print("This cell is already known")
                time.sleep(2)
                continue
            # Checks number of flags
            if len(flags) < MAX_MINE_NUM:
                print("You have set a flag!")
                time.sleep(2)

                # Appending flag to list
                flags.append([row, col])

                # Set flag display to user
                MINE_VALUES[row][col] = 'F'
                continue
            else:
                print("Flags finished")
                time.sleep(2)
                continue
        else:
            print("Incorrect input.. try again")
            time.sleep(2)
            instructions()

        if (val[0] > GRID_SIZE or val[0] < 1 or
            val[1] > GRID_SIZE or
                val[1] < 1):
            print("Incorrect input.. try again")
            time.sleep(2)
            instructions()
            continue
        # Get row and column numbers
        row = val[0]-1
        col = val[1]-1

        # If cell already flagged check
        if [row, col] in flags:
            flags.remove([row, col])

        # Game over when landing on a mine check
        if NUMBERS[row][col] == -1:
            MINE_VALUES[row][col] = 'M'  # M represents Mine
            display_mines()
            initialize_game_board()
            print("You have hit a mine... Game over!")
            time.sleep(1)
            over = True
            terminate_game()
            continue
        # If landing on a cell with no mines around it
        elif NUMBERS[row][col] == 0:
            global EMPTY_CELL
            EMPTY_CELL = []
            MINE_VALUES[row][col] = '0'
            adjoining_cells(row, col)
        # If landing on a cell with at least one adjoining_cells
        else:
            MINE_VALUES[row][col] = NUMBERS[row][col]

        # If game completed check
        if(check_game_concluded()):
            display_mines()
            initialize_game_board()
            print("Well done.. you have won! :)")
            time.sleep(1)
            over = True
            terminate_game()
            continue
        clear()


# Calling main function to run game
main()
