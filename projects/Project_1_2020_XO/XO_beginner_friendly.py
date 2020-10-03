def init_board():
    board = [[0, 1, 0, 1, 0],
             [2, 2, 2, 2, 2],
             [0, 1, 0, 1, 0],
             [2, 2, 2, 2, 2],
             [0, 1, 0, 1, 0]]
    return board


def pz():
    zones = ["void", (0, 0), (0, 2), (0, 4),
                     (2, 0), (2, 2), (2, 4),
                     (4, 0), (4, 2), (4, 4)]
    return zones


def draw_board(board):
    for i in board:
        for j in i:
            if j == 0:
                print(" ", end="")
            elif j == 1:
                print("|", end="")
            elif j == 2:
                print("-", end="")
            elif j == "x":
                print("X", end="")
            elif j == "o":
                print("O", end="")
        print("")


def player_x(b):
    zones = pz()
    entry = True
    while entry:
        i = int(input("Choose between 1 and 9: "))
        if b[zones[i][0]][zones[i][1]] == 0:
            b[zones[i][0]][zones[i][1]] = "x"
            entry = False
        else:
            print("Invalid entry...")


def player_o(b):
    zones = pz()
    entry = True
    while entry:
        i = int(input("Choose between 1 and 9: "))
        if b[zones[i][0]][zones[i][1]] == 0:
            b[zones[i][0]][zones[i][1]] = "o"
            entry = False
        else:
            print("Invalid entry...")


def win_conditions_x(b):
    z = pz()
# horizontal win
    if (b[z[1][0]][z[1][1]] == b[z[2][0]][z[2][1]] == b[z[3][0]][z[3][1]] == "x" or
        b[z[4][0]][z[4][1]] == b[z[5][0]][z[5][1]] == b[z[6][0]][z[6][1]] == "x" or
        b[z[7][0]][z[7][1]] == b[z[8][0]][z[8][1]] == b[z[9][0]][z[9][1]] == "x" or
# vertical win
        b[z[1][0]][z[1][1]] == b[z[4][0]][z[4][1]] == b[z[7][0]][z[7][1]] == "x" or
        b[z[2][0]][z[2][1]] == b[z[5][0]][z[5][1]] == b[z[8][0]][z[8][1]] == "x" or
        b[z[3][0]][z[3][1]] == b[z[6][0]][z[6][1]] == b[z[9][0]][z[9][1]] == "x" or
# diagonal win
        b[z[1][0]][z[1][1]] == b[z[5][0]][z[5][1]] == b[z[9][0]][z[9][1]] == "x" or
        b[z[3][0]][z[3][1]] == b[z[5][0]][z[5][1]] == b[z[7][0]][z[7][1]] == "x"):
        return True
    else:
        return False


def win_conditions_o(b):
    z = pz()
# horizontal win
    if (b[z[1][0]][z[1][1]] == b[z[2][0]][z[2][1]] == b[z[3][0]][z[3][1]] == "o" or
        b[z[4][0]][z[4][1]] == b[z[5][0]][z[5][1]] == b[z[6][0]][z[6][1]] == "o" or
        b[z[7][0]][z[7][1]] == b[z[8][0]][z[8][1]] == b[z[9][0]][z[9][1]] == "o" or
# vertical win
        b[z[1][0]][z[1][1]] == b[z[4][0]][z[4][1]] == b[z[7][0]][z[7][1]] == "o" or
        b[z[2][0]][z[2][1]] == b[z[5][0]][z[5][1]] == b[z[8][0]][z[8][1]] == "o" or
        b[z[3][0]][z[3][1]] == b[z[6][0]][z[6][1]] == b[z[9][0]][z[9][1]] == "o" or
# diagonal win
        b[z[1][0]][z[1][1]] == b[z[5][0]][z[5][1]] == b[z[9][0]][z[9][1]] == "o" or
        b[z[3][0]][z[3][1]] == b[z[5][0]][z[5][1]] == b[z[7][0]][z[7][1]] == "o"):
        return True
    else:
        return False


def start_game():
    game = init_board()
    no_win = True
    draw_board(game)
    while no_win:
        player_x(game)
        draw_board(game)
        if win_conditions_x(game):
            no_win = False
        if no_win:
            player_o(game)
            draw_board(game)
            if win_conditions_o(game):
                no_win = False
    if win_conditions_x(game):
        print("player X wins!!!")
    elif win_conditions_o(game):
        print("player O wins!!!")
    else:
        print("Draw!!!")


start_game()

