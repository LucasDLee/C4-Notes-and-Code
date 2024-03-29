# Step 1

import random

def run_game():
    ### ACTIVITY: ###
    # Make the following variables:
    # "player_score" and "computer_score" which start off as 0
    # "player_symbol" and "computer_symbol" which start off as -1
    # "play_again" which starts off as True
    player_score = 0
    computer_score = 0
    player_symbol = -1
    computer_symbol = -1
    play_again = True

    # Step 2
    while play_again == True:
        player_move = str(input("\nWhat is your move (R, P, S)? ")).upper()

        # Step 3
        # Assigning moves and symbols
        if player_move == 'R':
            player_move = "rock"
            player_symbol = 0
        elif player_move == 'P':
            player_move = "paper"
            player_symbol = 1
        elif player_move == 'S':
            player_move = "scissors"
            player_symbol = 2
        else:
            player_move = "invalid"
            player_symbol = -1

        # Step 4
        computer_symbol = random.randint(0,2)
        computer_move = ""

        ### ACTIVITY: ###
        # Make an if-statement that checks the following for the computer:

        # If my computer_symbol is 0, my computer_move will be "rock"
        # Else if my computer_symbol is 1, my computer_move will be "paper"
        # Else if my computer_symbol is 2, my computer_move will be scissors
        # Otherwise, set the computer_move to "unknown"

        if computer_symbol == 0:
            computer_move = "rock"
        elif computer_symbol == 1:
            computer_move = "paper"
        elif computer_symbol == 2:
            computer_move = "scissors"
        else:
            computer_move = "unknown"

        # Step 5
        # Checking who wins
        if player_symbol > computer_symbol: # player wins
            if computer_symbol == 0 and player_symbol == 2:
                computer_score = computer_score + 1
            else:
                player_score = player_score + 1

        ### ACTIVITY: ###
        # Complete the if-statement by checking if the computer wins using else-if
        # Else, print to the console: "It was a tie!"

        elif computer_symbol > player_symbol: # computer wins
            if player_symbol == 0 and computer_symbol == 2:
                player_score = player_score + 1
            else:
                computer_score = computer_score + 1
        else:
            print("It was a tie!")

        # Step 6
        print("The player's move was " + player_move + " and the computer's move was " + computer_move)
        print("The player's score is " + str(player_score))
        print("The computer's score is " + str(computer_score))
        
        # Step 7
        play_again = str(input("Do you want to play again (Y or N)? ")).upper()
        if play_again == 'N':
            play_again = False
            print("\nGame has been terminated")
        else:
            play_again = True

run_game()