def get_location_of_king(board):
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[i]):
            if board[i][j] == "K":
                return (i, j)
            j += 1
        i += 1


def move_right(board):
    i = get_location_of_king(board)[0]
    j = get_location_of_king(board)[1]

    board[i][j] = " "
    board[i][j+1] = "K"


def tests_for_get_location():
    # 1) Test for get_location_of_king
    test_map = \
        [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", "K", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]
    assert get_location_of_king(test_map) == (2, 2)
    test_map = \
        [["K", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]
    assert get_location_of_king(test_map) == (0, 0)


def tests_for_move_right():
    # 2) Tests for move_right
    test_map = \
        [["K", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]
    move_right(test_map)
    assert test_map == \
        [[" ", "K", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]

    move_right(test_map)
    move_right(test_map)
    assert test_map == \
           [[" ", " ", " ", "K", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]]


tests_for_get_location()
tests_for_move_right()
