from tic_tac_toe_solution import *

# TODO: uncomment assertion tests for functions that you have finished implementing
#  If when running this file you don't get any assertion error, this means your code (probably) works.
#  You are not allowed to edit anything of this file !

######################
# 1) get_new_board() #
######################
# assert get_new_board(3) == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# assert get_new_board(4) == [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]
# assert get_new_board(1) == [[" "]]
# assert get_new_board(0) == []
# assert get_new_board(-7) == []

#########################################
# 2) add_x_at_position(board, position) #
#########################################
# board = get_new_board(3)
# add_x_at_position(board, (1, 2))
# assert board == [[" ", " ", " "],
#                  [" ", " ", "X"],
#                  [" ", " ", " "]]
# add_x_at_position(board, (0, 1))
# assert board == [[" ", "X", " "],
#                  [" ", " ", "X"],
#                  [" ", " ", " "]]
# add_x_at_position(board, (5454, 959859))
# assert board == [[" ", "X", " "],
#                  [" ", " ", "X"],
#                  [" ", " ", " "]]
# add_x_at_position(board, (-7, 0))
# assert board == [[" ", "X", " "],
#                  [" ", " ", "X"],
#                  [" ", " ", " "]]

#########################################
# 3) add_o_at_position(board, position) #
#########################################
# board = get_new_board(3)
# add_o_at_position(board, (1, 2))
# assert board == [[" ", " ", " "],
#                  [" ", " ", "O"],
#                  [" ", " ", " "]]
# add_o_at_position(board, (0, 1))
# assert board == [[" ", "O", " "],
#                  [" ", " ", "O"],
#                  [" ", " ", " "]]
# add_o_at_position(board, (5454, 959859))
# assert board == [[" ", "O", " "],
#                  [" ", " ", "O"],
#                  [" ", " ", " "]]
# add_o_at_position(board, (-7, 0))
# assert board == [[" ", "O", " "],
#                  [" ", " ", "O"],
#                  [" ", " ", " "]]

######################################
# 4) get_board_representation(board) #
######################################
# board = get_new_board(3)
# board_representation = get_board_representation(board)
# print(board_representation)
# assert board_representation == " | | \n" \
#                                "-----\n" \
#                                " | | \n" \
#                                "-----\n" \
#                                " | | \n"  # This is in fact a one line string, I am just simplifying the view.
# add_x_at_position(board, (1, 2))
# board_representation = get_board_representation(board)
# assert board_representation == " | | \n" \
#                                "-----\n" \
#                                " | |X\n" \
#                                "-----\n" \
#                                " | | \n"
# add_o_at_position(board, (0, 0))
# board_representation = get_board_representation(board)
# assert board_representation == "O| | \n" \
#                                "-----\n" \
#                                " | |X\n" \
#                                "-----\n" \
#                                " | | \n"
# add_x_at_position(board, (1, 1))
# board_representation = get_board_representation(board)
# assert board_representation == "O| | \n" \
#                                "-----\n" \
#                                " |X|X\n" \
#                                "-----\n" \
#                                " | | \n"
# add_o_at_position(board, (1, 0))
# board_representation = get_board_representation(board)
# assert board_representation == "O| | \n" \
#                                "-----\n" \
#                                "O|X|X\n" \
#                                "-----\n" \
#                                " | | \n"
# board = get_new_board(2)
# board_representation = get_board_representation(board)
# assert board_representation == " | \n" \
#                                "---\n" \
#                                " | \n"
# board = get_new_board(4)
# board_representation = get_board_representation(board)
# assert board_representation == " | | | \n" \
#                                "-------\n" \
#                                " | | | \n" \
#                                "-------\n" \
#                                " | | | \n" \
#                                "-------\n" \
#                                " | | | \n"


#######################
# 5) is_game_finished #
#######################
# board = get_new_board(3)
# assert not is_game_finished(board)
# assert not is_game_finished([[" ", " ", " "],
#                              [" ", " ", " "],
#                              [" ", " ", " "]])
# assert not is_game_finished([[" ", " ", " "],
#                              [" ", " ", "X"],
#                              [" ", " ", " "]])
# assert not is_game_finished([[" ", " ", " "],
#                              ["O", "X", "X"],
#                              [" ", " ", " "]])
# assert not is_game_finished([["O", "O", " "],
#                              ["O", "X", "X"],
#                              [" ", "X", "X"]])
# assert not is_game_finished([["X", " ", "X"],
#                              ["O", "O", "X"],
#                              ["O", "X", "O"]])
# assert not is_game_finished([["X", "O", "X"],
#                              ["O", "O", "X"],
#                              ["O", "X", " "]])
# assert is_game_finished([[" ", " ", "X"],
#                          [" ", " ", "X"],
#                          [" ", " ", "X"]])
# assert is_game_finished([[" ", "O", "X"],
#                          [" ", "O", "X"],
#                          [" ", " ", "X"]])
# assert is_game_finished([["O", " ", "X"],
#                          [" ", "O", "X"],
#                          [" ", " ", "O"]])
# assert is_game_finished([["X", "X", "O"],
#                          ["X", "O", "X"],
#                          ["O", "X", "O"]])
# assert is_game_finished([["X", "X", "X"],
#                          ["O", "O", " "],
#                          ["O", "O", "X"]])
# assert is_game_finished([["O", " ", " "],
#                          ["X", "O", "X"],
#                          ["O", "X", "O"]])
# assert not is_game_finished([["O", "X", " ", "O"],
#                              ["X", "O", "X", "X"],
#                              ["O", "X", "O", "X"],
#                              ["O", "O", "O", "X"]])  # This 4x4 board is not finished because there is no row of 4 !!
# assert is_game_finished([["O", "X", "O", "O"],
#                          ["X", "O", "X", "X"],
#                          ["O", "X", "O", "X"],
#                          ["O", "O", "O", "X"]])

#################
# 6) get_winner #
#################
# assert get_winner([[" ", " ", " "],
#                    [" ", " ", " "],
#                    [" ", " ", " "]]) is None
# assert get_winner([[" ", " ", " "],
#                    [" ", "X", " "],
#                    [" ", " ", " "]]) is None
# assert get_winner([[" ", "X", "O"],
#                    [" ", "X", " "],
#                    ["O", " ", "O"]]) is None
# assert get_winner([["O", "X", "X"],
#                    ["O", "X", "X"],
#                    [" ", "O", "O"]]) is None
# assert get_winner([["X", "X", "O"],
#                    ["O", "O", "X"],
#                    ["X", "X", "O"]]) is None
# assert get_winner([["O", "X", "O"],
#                    [" ", "X", "O"],
#                    [" ", "X", " "]]) == "player X"
# assert get_winner([["O", "X", "O"],
#                    [" ", "X", "O"],
#                    ["X", "O", "O"]]) == "player O"
# assert get_winner([["O", "X", "O"],
#                    ["X", "X", "X"],
#                    ["O", "O", "X"]]) == "player X"
# assert get_winner([["O", "X", "X"],
#                    ["X", "O", "O"],
#                    ["X", "X", "O"]]) == "player O"
# assert get_winner([["O", "O", "X"],
#                    [" ", "X", "O"],
#                    ["X", "X", "O"]]) == "player X"
# assert get_winner([["O", "X", "O", "O"],
#                    ["X", "O", "X", "X"],
#                    ["O", "X", "O", "X"],
#                    ["O", "O", "O", "X"]]) is None  # This 4x4 board has no winner because there is no row of 4 !!
