import random

def run_game():
    player_score = 0
    computer_score = 0
    player_symbol = -1
    computer_symbol = -1
    play_again = True

    while play_again:
        player_move = str(input("\nWhat is your move (R, P, S)? ")).upper()

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
            player_symbol = -1
            player_move = "invalid"

        computer_symbol = random.randint(0,2)
        computer_move = ""

        ### ACTIVITY: ###
        # Make an if-statement that checks the following for the computer:

        # If my computer_symbol is 0, my computer_move will be "rock"
        # Else if my computer_symbol is 1, my computer_move will be "paper"
        # Else if my computer_symbol is 2, my computer_move will be scissors

        if computer_symbol == 0:
            computer_move = "rock"
        elif computer_symbol == 1:
            computer_move = "paper"
        elif computer_symbol == 2:
            computer_move = "scissors"
        else:
            computer_move = "unknown"

        if player_symbol > computer_symbol: # player wins
            if computer_symbol == 0 and player_symbol == 2:
                computer_score = computer_score + 1
            else:
                player_score = player_score + 1

        ### ACTIVITY: ###
        # Complete the if-statement by checking if the computer wins using else-if
        # Else, print to the console: "It was a tie!"

        elif computer_symbol > player_symbol:
            if player_symbol == 0 and computer_symbol == 2:
                player_score = player_score + 1
            else:
                computer_score = computer_score + 1
        else:
            print("It was a tie!")

        print("The player's move was " + player_move + " and the computer's move was " + computer_move)
        print("The player's score is " + str(player_score))
        print("The computer's score is " + str(computer_score))
        play_again = str(input("Do you want to play again (Y or N)?" ))

        if play_again == 'N':
            play_again = False
        else:
            play_again = True

run_game()