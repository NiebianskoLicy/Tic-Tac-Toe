import os

spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
# drawing board with spots dictionary, allows to easy replace numbers in board
def draw_board(spots):
    board = f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|"
    print(board)

# replaces number with x/o
def draw_figure(field_number, player_figure):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # return True if figure is already written
    if spots[field_number] in numbers:
        spots[int(field_number)] = player_figure
        return False
    else:
        return True

# check for win
def win(spots):
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
p1 = input("Would you like to start with 'x' or 'o'?: ")
p2 = ""
if p1 == "x":
    p2 = "o"
elif p1 == "o":
    p2 == "x"
else:
    print("Only choose 'x' or 'o'")
    p1 = input("Would you like to start with 'x' or 'o'?: ")

# tracking numbers of turns
turn = 0
complete = False
game = True
clear = True
while game:
    # clear screen
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    # switching turns
    if (turn % 2) == 0:
        player = p1
    else:
        player = p2

    draw_board(spots)

    draw = input(f"'{player}' choose field(or enter 'q' to quit): ")

    # checking if player want to stop game
    if draw == "q":
        game = False
    # end game with 8 turns (full board)
    elif turn == 8:
        print("game end")
        game = False
    # TODO
    elif draw in spots.values():
        t_or_n = draw_figure(int(draw), player)
        # if player choose wrong field number
        if t_or_n:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Choose only free field numeber!!")
            clear = False
        elif not t_or_n:
            clear = True
            turn += 1
            
    # if player write in wrong field number
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        clear = False
        print("Choose only free field number")

    # if someone wins then end the game
    if win(spots): game, complete = False, True

# clear screen and drawing board for seeing end game
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# writting winner or not if its draw
if complete: print(f"{player} wins!")
else: print("No winner!")

# TODO
again = input("\nWould u like to play again? (Yes/No)").lower()
if again == "yes" or again == "y":
    game = True
    complete = False
elif again == "no" or again == "n":
    print("Thanks for playing!")
else:
    print("Write only yes or no")