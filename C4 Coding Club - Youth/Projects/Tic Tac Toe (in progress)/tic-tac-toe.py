global game_tile
game_tile = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def check_move(move, player):
    player_symbol = ""
    if player == 1:
        player_symbol = 'X'
    else:
        player_symbol = 'O'

    if game_tile[move] == move:
        game_tile[move] = player_symbol
        print(game_tile)
        return True

    print(game_tile)
    return False

def show_board():
    line1 = "{0} | {1} | {2}".format(game_tile[0], game_tile[1], game_tile[2])
    line2 = "{0} | {1} | {2}".format(game_tile[3], game_tile[4], game_tile[5])
    line3 = "{0} | {1} | {2}".format(game_tile[6], game_tile[7], game_tile[8])
    divider1 =""
    divider2 = ""
    for x in range(len(line1)):
        divider1 += "-"
        divider2 += "-"

    show_board = ("{l1}\n{d1}\n{l2}\n{d2}\n{l3}").format(l1 = line1, l2 = line2, l3 = line3, d1 = divider1, d2 = divider2)
    print(show_board)

### ACTIVITY: ###

# Description: We need to check if someone has won everytime a new tile is placed in the horizontal, vertical, and diagonal directions
# 1) Make a function called "check_winner". This function takes NO parameters
# 2) First, let's make a for-loop that runs 3 times

def check_winner():

    return

def run_game():
    valid_move = True
    game_on = input("Do you want to start the game? ")
    while game_on:
        print("Player 1\n---------------------")
        player_1_move = int(input("Which tile would you like to use:"))
        valid_move = check_move(player_1_move, 1)
        while valid_move != False:
            player_1_move = int(input("That tile is taken. Which tile would you like to use:"))
            valid_move = check_move(player_1_move, 1)
        
        print("Player 2\n---------------------")
        player_2_move = int(input("Which tile would you like to use:"))
        valid_move = check_move(player_2_move, 2)
        while valid_move != False:
            player_2_move = int(input("That tile is taken. Which tile would you like to use:"))
            valid_move = check_move(player_2_move, 2)
        
        show_board()
    return
run_game()