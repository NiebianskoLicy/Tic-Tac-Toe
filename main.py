import os
from methods import draw_board, draw_figure, check_for_win, check_turn

spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

pla_choi = player_choosing_fig()

# TODO 
def the_game(spots):
    complete = False
    game = True
    clear = True
    # Tracking number of rounds
    turn = 0

    while game:
        # clear screen
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')

        draw_board(spots)

        draw = input(f"'{check_turn(turn=turn)}' choose field(or enter 'q' to quit): ")

        # allowing player to quit game
        if draw == "q":
            quit()
        # game ends after board is full occupied
        elif turn == 8:
            print("game end")
            game = False
        elif draw_figure(int(draw), check_turn(turn=turn), spots):
            clear = True
            turn += 1
                
        # feedback after player select the occupied spots
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            clear = False
            print("Choose only not occupied spot\n")

        # game ends if someone wins
        if check_for_win(spots): game, complete = False, True

    # clear screen and drawing a board for seeing end game
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    # feedback on who win or, if its draw
    if complete: print(f"{player} wins!")
    else: print("No winner!")
    
    # allowing to play again 
    again = input("\nWould u like to play again? (Yes/No)").lower()
    if again == "yes" or again == "y":
        game = True
        complete = False
        spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
        the_game(spots)
    elif again == "no" or again == "n":
        print("\nThanks for playing!\n")
    else:
        print("Write only yes or no")

the_game(spots)
