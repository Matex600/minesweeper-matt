"""
Imported modules     describe file briefly.
"""
import random
import os

# Size of game grid (6x6)
GRID_SIZE = 6

#  Visible values of the grid
mine_values = [[' ' for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

# Actual (hidden) values of the grid
numbers = [[0 for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

# Tracking umber of mines already set starts at 0
NUM_MINES_PRESENT = 0

# Number of mines in play grid
MAX_MINE_NUM = 6

# Flagged positions
flags = []


# Welcome message and username prompt
print("--------- Welcome to Minesweeper ---------")
print(" --------- --------- --------- ---------")
print("------ Start by entering username! ------")

username = input()


# Message after username input with game instructions
def instructions():
    """
    Game instruction function
    """
    print("----- Welcome, " + username + ", good luck & have fun! -----\n")
    print('''Game instructions! \n
        1. Game board contains 6 rows, columns and mines.
        2. Enter a number between 1 and 6 for row
            and column. (Example: "3, 5")
        3. Hitting a mine results in game over\n''')


def initialize_game_board():
    """
    Function defines global variables and
    creates the game board using the value GRID_SIZE
    for columns and rows through the use of for loops
    """
    print("    Game starting ... \n")

    print()
    # Layout of Minesweeper game area
    cell_block = "   "
    for i in range(GRID_SIZE):
        cell_block = cell_block + "     " + str(i + 1)
    print(cell_block)

    # For loop creates squares in the grid using | and _
    for r in range(GRID_SIZE):
        cell_block = "     "
        if r == 0:
            for col in range(GRID_SIZE):
                cell_block = cell_block + "______"
            print(cell_block)

        cell_block = "     "
        for col in range(GRID_SIZE):
            cell_block = cell_block + "|     "
        print(cell_block + "|")

        cell_block = "  " + str(r + 1) + "  "
        for col in range(GRID_SIZE):
            cell_block = cell_block + "|  " + str(mine_values[r][col]) + "  "
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
    
    NUM_MINES_PRESENT = 0
    
    while NUM_MINES_PRESENT < MAX_MINE_NUM:

        # Random number for grid positions
        grid_positions = random.randint(0, GRID_SIZE*GRID_SIZE - 1)

        # Generate row and column from numbers in grid
        r = grid_positions // GRID_SIZE
        col = grid_positions % GRID_SIZE

        # Add a mine if there are none on the grid
        if numbers[r][col] != - 1:
            NUM_MINES_PRESENT = NUM_MINES_PRESENT + 1
            numbers[r][col] = - 1


def actual_board_values():
    """
    This function sets up board values that are hidden from
    the player and work in the background, checking the board for
    presence of mines using a for loop
    """

    # Loop that counts every cell in the grid
    for r in range(GRID_SIZE):
        for col in range(GRID_SIZE):
          
            # Skips check if a mine is present
            if numbers[r][col] == - 1:
                continue

            # Checks input above
            if r > 0 and numbers[r-1][col] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks input below
            if r < GRID_SIZE-1 and numbers[r+1][col] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks left input
            if col > 0 and numbers[r][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks right input
            if col < GRID_SIZE - 1 and numbers[r][col+1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks top left input
            if r > 0 and col > 0 and numbers[r-1][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks top right input
            if r > 0 and col < GRID_SIZE - 1 and numbers[r-1][col+1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks bottom left input
            if r < GRID_SIZE - 1 and col > 0 and numbers[r+1][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks bottom right input
            if (r < GRID_SIZE - 1
                and col < GRID_SIZE - 1
                    and numbers[r+1][col+1] == -1):
                numbers[r][col] = numbers[r][col] + 1


def adjoining_cells(r, col):
    """
    This is a recursive function to display all empty cells
    marked with (0)
    """
    global EMPTY_CELL

    # If cell is empty
    if [r, col] not in EMPTY_CELL:

        # Mark visited cell
        EMPTY_CELL.append([r, col])

        # 0 value cell
        if numbers[r][col] == 0:

            # Show user
            # mine_values[r][col] = numbers[r][col]
            # x = r-1
            # y = col-1
            # # Recursive for adjoining cells
            # while x <= r+1:
            #     while y <= col+1:
            #         print()
            #         y += 1
            #     x += 1
            if r > 0:
                adjoining_cells(r-1, col)
            if r < GRID_SIZE-1:
                adjoining_cells(r+1, col)
            if col > 0:
                adjoining_cells(r, col-1)
            if col < GRID_SIZE-1:
                adjoining_cells(r, col+1)
            if r > 0 and col > 0:
                adjoining_cells(r-1, col-1)
            if r > 0 and col < GRID_SIZE-1:
                adjoining_cells(r-1, col+1)
            if r < GRID_SIZE-1 and col > 0:
                adjoining_cells(r+1, col-1)
            if r < GRID_SIZE-1 and col < GRID_SIZE-1:
                adjoining_cells(r+1, col+1)
        # If not empty cell
        if numbers[r][col] != 0:
            mine_values[r][col] = numbers[r][col]


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

    for r in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if numbers[r][col] == - 1:
                mine_values[r][col] = 'M'


def check_game_concluded():
    """
    Function to check if game has conculded
    """
    NUM_MINES_PRESENT = 0

    # Loop to check each square in grid
    for r in range(GRID_SIZE):
        for col in range(GRID_SIZE):

            # If the cell contains mine
            if mine_values[r][col] != ' ' and mine_values[r][col] != 'F':
                NUM_MINES_PRESENT = NUM_MINES_PRESENT + 1

    if NUM_MINES_PRESENT == GRID_SIZE * GRID_SIZE - MAX_MINE_NUM:
        return True
    else:
        return False


def main():
    """
    Main function that runs the game
    from start to end
    """
    global EMPTY_CELL

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
        player_input = input('''Enter a row number
        followed by a space and column number = ''').split()

        # Standard player input check
        if len(player_input) == 2:
            try:
                val = list(map(int, player_input))
                print("Input selected...", player_input)
            except ValueError:
                print("Input is incorrect.. please make correct selection")
                instructions()
                continue
        # Flag input check
        elif len(player_input) == 3:
            if player_input[2] != 'F' and player_input[2] != 'f':
                print("Incorrect flag input.. try again")
                instructions()
                continue
            try:
                val = list(map(int, player_input[:2]))
            except ValueError:
                print("Incorrect flag input.. try again")
                instructions()
                continue
            if val[0] > GRID_SIZE or val[0] < 1 or val[1] > GRID_SIZE or val[1] < 1:
                print("Incorrect flag input.. try again")
                instructions()
                continue
            # Getting row and column numbers
            r = val[0]-1
            col = val[1]-1

            # If grid cell already flagged by user
            if [r, col] in flags:
                print("This cell has already been flagged")
                continue
            # If grid cell already displayed to user
            if mine_values[r][col] != ' ':
                print("This cell is already known")
                continue
            # Checks number of flags
            if len(flags) < MAX_MINE_NUM:
                print("You have set a flag!")

                # Appending flag to list
                flags.append([r, col])

                # Set flag display to user
                mine_values[r][col] = 'F'
                continue
            else:
                print("Flags finished")
                continue
        else:
            print("Incorrect flag input.. try again")
            instructions()

        if val[0] > GRID_SIZE or val[0] < 1 or val[1] > GRID_SIZE or val[1] < 1:
            print("Incorrect flag input.. try again")
            instructions()
            continue
        # Get row and column numbers
        r = val[0]-1
        col = val[1]-1

        # If cell already flagged check
        if [r, col] in flags:
            flags.remove([r, col])

        # Game over when landing on a mine check
        if numbers[r][col] == -1:
            mine_values[r][col] = 'M'  # M represents Mine
            display_mines()
            initialize_game_board()
            print("You have hit a mine... Game over!")
            over = True
            continue
        # If landing on a cell with no mines around it
        elif numbers[r][col] == 0:
            EMPTY_CELL = []
            mine_values[r][col] = '0'
            adjoining_cells(r, col)
        # If landing on a cell with at least one adjoining_cells
        else:
            mine_values[r][col] = numbers[r][col]

        # If game completed check
        if(check_game_concluded()):
            display_mines()
            initialize_game_board()
            print("Well done.. you have won! :)")
            over = True
            continue
        clear()


main()
