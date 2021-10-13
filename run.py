# Imported modules
import random
import os


# Size of game grid (6x6)
grid_size = 6

#  Visible values of the grid
mine_values = [[' ' for y in range(grid_size)] for x in range(grid_size)]

# Actual (hidden) values of the grid
numbers = [[0 for y in range(grid_size)] for x in range(grid_size)]

# Tracking umber of mines already set starts at 0
num_mines_present = 0

# Number of mines in play grid
max_mine_num = 6

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
    creates the game board using the value j
    for columns and rows through the use of for loops
    """
    print("    Game starting ... \n")

    print()
    # Layout of Minesweeper game area
    cell_block = "   "
    for i in range(grid_size):
        cell_block = cell_block + "     " + str(i + 1)
    print(cell_block)

    # For loop creates squares in the grid using | and _
    for r in range(grid_size):
        cell_block = "     "
        if r == 0:
            for col in range(grid_size):
                cell_block = cell_block + "______"
            print(cell_block)

        cell_block = "     "
        for col in range(grid_size):
            cell_block = cell_block + "|     "
        print(cell_block + "|")

        cell_block = "  " + str(r + 1) + "  "
        for col in range(grid_size):
            cell_block = cell_block + "|  " + str(mine_values[r][col]) + "  "
        print(cell_block + "|")

        cell_block = "     "
        for col in range(grid_size):
            cell_block = cell_block + "|_____"
        print(cell_block + "|")

    print()
    

def inject_bombs():
    """
    This function stores data and values from the mines
    and flags
    """

    num_mines_present = 0
    while num_mines_present < max_mine_num:

        # Random number for grid positions
        grid_positions = random.randint(0, grid_size*grid_size - 1)

        # Generate row and column from numbers in grid
        r = grid_positions // grid_size
        col = grid_positions % grid_size

        # Add a mine if there are none on the grid
        if numbers[r][col] != - 1:
            num_mines_present = num_mines_present + 1
            numbers[r][col] = - 1


def actual_board_values():
    """
    This function sets up board values that are hidden from
    the player and work in the background, checking the board for
    presence of mines using a for loop
    """

    # Loop that counts every cell in the grid
    for r in range(grid_size):
        for col in range(grid_size):
          
            # Skips check if a mine is present
            if numbers[r][col] == - 1:
                continue

            # Checks input above
            if r > 0 and numbers[r-1][col] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks input below
            if r < grid_size-1 and numbers[r+1][col] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks left input
            if col > 0 and numbers[r][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks right input
            if col < grid_size - 1 and numbers[r][col+1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks top left input
            if r > 0 and col > 0 and numbers[r-1][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks top right input
            if r > 0 and col < grid_size - 1 and numbers[r-1][col+1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks bottom left input
            if r < grid_size - 1 and col > 0 and numbers[r+1][col-1] == - 1:
                numbers[r][col] = numbers[r][col] + 1

            # Checks bottom right input
            if (r < grid_size - 1
                and col < grid_size - 1
                    and numbers[r+1][col+1] == -1):
                numbers[r][col] = numbers[r][col] + 1


def main():
    """
    Main function that runs the game
    from start to end
    """
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
            if val[0] > grid_size or val[0] < 1 or val[1] > grid_size or val[1] < 1:
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
            if len(flags) < max_mine_num:
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

        if val[0] > grid_size or val[0] < 1 or val[1] > grid_size or val[1] < 1:
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
            mine_values[r][col] = 'M' # M represents Mine
            inject_bombs()
            initialize_game_board()
            print("You have hit a mine... Game over!")
            over = True
            continue


main()
