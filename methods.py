# drawing board with spots dictionary, allows to easy replace numbers in board
def draw_board(spots):
    board = f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|"
    print(board)


# replaces number on the board with figure(x/o)
def draw_figure(field_number, player_figure, spots):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # return False if spot is already occupied
    if spots[field_number] in numbers:
        spots[int(field_number)] = player_figure
        return True
    else: return False
    

# checking for win situation
def check_for_win(spots):
    if (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
        return True

    elif (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
        return True

    elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
        return True

    else: return False

# players choosing figure
def check_turn(turn):
    if (turn % 2) == 0: return "O"
    else: return "X"