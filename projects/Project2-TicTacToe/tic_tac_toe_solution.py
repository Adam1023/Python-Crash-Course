import os
import platform


def get_new_board(dimension):
    """
    Return a multidimensional list that represents an empty board (i.e. string with a space at every position).
    :param: dimension: integer representing the nxn dimension of your board.
            For example, if dimension is 3, you should return a 3x3 board
    :return: For example if dimension is 3x3, you should return:
                --> [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]
    """
    result = []
    for _ in range(dimension):
        result.append([])
        for _ in range(dimension):
            result[-1].append(" ")

    return result


def is_position_legal(position, board):
    """Return whether the given position is a legal position for given board."""
    return 0 <= position[0] < len(board) and 0 <= position[1] < len(board)


def add_x_at_position(board, position):
    """
    Edit the given board by adding "X" to the given position. *Don't* return anything! Just edit the board argument.
    For example if board == [["", "", ""], ["", "", ""], ["", "", ""]] and position == (1,2), the board should become:
    --> [["", "", ""],
         ["", "", "X"],
         ["", "", ""]]
    :param board: multidimensional list representing the current state of the game board
    :param position: a tuple with as first element the row number and as second element the column number.
           For example: (2,3) --> the position at the 3rd row and 4th column
    """
    if is_position_legal(position, board):
        board[position[0]][position[1]] = "X"


def add_o_at_position(board, position):
    """
    Exactly the same as "add_x_at_position()" but instead of adding "X" you add "O" (big o, not zero 0).
    If you are smart you can come up with a solution to avoid code duplication with previous function. Otherwise it's
    okay if you make the same work a second time in this function.
    """
    if is_position_legal(position, board):
        board[position[0]][position[1]] = "O"


def get_board_representation(board):
    """
    Return a string representing the entire board as how you are supposed to print it.
    Outside the function you should be able to do the following in order to print the string:
    print(get_board_representation(board)).

    For more details about how exactly the representation should look like, take a look at the test file.
    :param board: A multidimensional list representing the board
    :return a string representation of the current state of the given board (see tests for details)
    """
    result = ""

    # Add all rows except the last one
    for i in range(len(board)-1):
        row = board[i]
        # Add all elements of the row except the last one:
        for j in range(len(row)-1):
            result += row[j] + "|"
        # Add last element of the row:
        result += row[-1] + "\n" + "-" * (len(row)*2-1) + "\n"
    # Add last row (without adding the delimiter "-----" under it):
    row = board[-1]
    for j in range(len(row)-1):
        result += row[j] + "|"
    result += row[-1] + "\n"
    return result


def is_game_finished(board):
    """
    Return true if the game is finished and false if it isn't.
    A game is finished when one of two players won, or when all the cells of the board were filled.
    :param board: A multidimensional list representing the board
    :return: True or False, signaling whether the game is finished.
    """
    if get_winner(board) is not None:
        return True

    for row in board:
        for col in row:
            if col == " ":
                return False

    return True


def list_contains_only_xs(lst):
    """Check whether the given list contains only x's"""
    for elem in lst:
        if elem != "X":
            return False

    return True


def list_contains_only_os(lst):
    """Check whether the given list contains only o's"""
    for elem in lst:
        if elem != "O":
            return False

    return True


def down_diagonal_contains_only_xs(board):
    """Check whether the going down diagonal contains only xs"""
    for i in range(len(board)):
        if board[i][i] != "X":
            return False
    return True


def down_diagonal_contains_only_os(board):
    """Check whether the going down diagonal contains only os"""
    for i in range(len(board)):
        if board[i][i] != "O":
            return False
    return True


def up_diagonal_contains_only_xs(board):
    """Check whether the going up diagonal contains only xs"""
    i = len(board) - 1
    j = 0
    while i >= 0 and j < len(board):
        if board[i][j] != "X":
            return False
        i -= 1
        j += 1

    return True


def up_diagonal_contains_only_os(board):
    """Check whether the going up diagonal contains only os"""
    i = len(board) - 1
    j = 0
    while i >= 0 and j < len(board):
        if board[i][j] != "O":
            return False
        i -= 1
        j += 1

    return True


def get_winner(board):
    """
    Return the winner of this game based on given board.
    If the winner is player X, you should return "player X".
    If the winner is player O, you should return "player O".
    If this game is not yet finished or if there is no winner, you should return None (not a string, it's valid Python).

    :param board: A multidimensional list representing the board
    :return: "player X" or "player O" or None
    """
    # Check if an entire row is full
    for row in board:
        if list_contains_only_xs(row):
            return "player X"
        elif list_contains_only_os(row):
            return "player O"

    # Check if an entire column is full
    for i in range(len(board)):
        if list_contains_only_xs([row[i] for row in board]):
            return "player X"
        elif list_contains_only_os([row[i] for row in board]):
            return "player O"

    # Check for the two diagonals
    if up_diagonal_contains_only_xs(board) or down_diagonal_contains_only_xs(board):
        return "player X"
    elif up_diagonal_contains_only_os(board) or down_diagonal_contains_only_os(board):
        return "player O"

    return None


def get_i_j_from_player(board):
    i = input("Row (starts from 0): ")
    while not i.isdigit() or int(i) >= len(board):
        print(f"Your input should be a number between 0 and {len(board) - 1} (both included)!")
        i = input("Row (starts from 0): ")
    j = input("Column (starts from 0): ")
    while not j.isdigit() or int(j) >= len(board):
        print(f"Your input should be a number between 0 and {len(board) - 1} (both included)!")
        j = input("Column (starts from 0): ")
    i = int(i)
    j = int(j)
    return i, j


def player_x(board):
    """
    Let player X play his turn. You should first ask him for input. Ask him for the row and the column where he wants
    to put the next X. You should be cautious with every case:
    * If the given position is empty, you should place the X (don't return anything, just edit the given board).
    * If the position is outside the boundaries of the given board, you shouldn't edit the board and should print a
      message to inform the user that his input is invalid and give him another chance.
    * If the given position is already occupied, you should also not edit the board and should print a message to inform
      the user that the position is already occupied and give him another chance.

    There are no tests for this function. So make sure you find a way to test it yourself.

    :param board: A multidimensional list representing the board
    """
    print("-Player X-\n")

    i, j = get_i_j_from_player(board)

    if 0 <= i < len(board) and 0 <= j < len(board) and board[i][j] == " ":
        board[i][j] = "X"
    else:
        print("That position is already occupied. Try again !")
        player_x(board)


def player_o(board):
    """
    Let player O play his turn. Just like player_x. And if you are smart, you will make an extra helper
    function to avoid code duplication.

    There are no tests for this function. So make sure you find a way to test it yourself.
    """
    print("-Player O-\n")

    i, j = get_i_j_from_player(board)

    if 0 <= i < len(board) and 0 <= j < len(board) and board[i][j] == " ":
        board[i][j] = "O"
    else:
        print("That position is already occupied. Try again !")
        player_o(board)


if __name__ == '__main__':
    # Everything below is already implemented for you. Don't edit it ! It represents the logic of the game using your
    # functions. This should only work correctly if your functions work correctly.

    print("############################")
    print("# Welcome to TIC TAC TOE ! #")
    print("############################")

    # Ask for the board dimension
    dimension = input("Choose a dimension for your board: ")
    while not dimension.isdigit():
        print("You did not give a (positive) integer, Try again !")
        dimension = input("Choose a dimension for your board: ")

    # Generate this new board and print its representation
    board = get_new_board(int(dimension))
    print(get_board_representation(board))

    # Ask for user input by alternating between both players (X and O)
    alternate = 0
    while not is_game_finished(board):
        if alternate == 0:
            player_o(board)
            alternate = 1
        elif alternate == 1:
            player_x(board)
            alternate = 0

        # Clear everything and print the new board representation
        if platform.system() == "Windows":
            os.system('cls')
        print(get_board_representation(board))

    # Print who's the winner (if any)
    winner = get_winner(board)
    if winner is None:
        print("DRAW!\nThis game is finished and there is no winner.")
    else:
        print(f"FINISHED!\nThe winner of this game is: {winner} !")
