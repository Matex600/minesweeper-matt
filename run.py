import random
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("--------- Welcome to Minesweeper ---------")
print(" --------- --------- --------- ---------")
print("------ Start by entering username! ------")

username = input()

print("----- Welcome, " + username + ", good luck & have fun! -----\n")

def initialize_game_board(i, j):
    """
    Create game board using columns and rows
    """
    print("    Game started ... \n")
    board = [["." for row in range(i)] for column in range(j)]
    for row in board:
        print(" ".join(str(cell) for cell in row))
        print("")
# def inject_bombs():
"""
"""
# def player_input():
"""
"""
# def game_over():
"""
"""
def main():
    initialize_game_board(12, 6)
main()    