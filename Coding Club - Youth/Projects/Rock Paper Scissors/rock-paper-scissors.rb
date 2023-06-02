# Step 1

def run_game()
    ### ACTIVITY: ###
    # Make the following variables:
    # "player_score" and "computer_score" which start off as 0
    # "player_symbol" and "computer_symbol" which start off as -1
    # "play_again" which starts off as true
    player_score = 0
    computer_score = 0
    player_symbol = -1
    computer_symbol = -1
    play_again = true

    # Step 2
    while play_again == true
        puts "\nWhat is your move (R, P, S)?"
        player_move = gets.chomp.upcase

        # Step 3
        # Assigning moves and symbols
        if player_move == 'R'
            player_move = "rock"
            player_symbol = 0
        elsif player_move == 'P'
            player_move = "paper"
            player_symbol = 1
        elsif player_move == 'S'
            player_move = "scissors"
            player_symbol = 2
        else
            player_move = "invalid"
            player_symbol = -1
        end

        # Step 4
        computer_symbol = rand(0..2)
        computer_move = ""

        ### ACTIVITY: ###
        # Make an if-statement that checks the following for the computer:

        # If my computer_symbol is 0, my computer_move will be "rock"
        # Else if my computer_symbol is 1, my computer_move will be "paper"
        # Else if my computer_symbol is 2, my computer_move will be "scissors"
        # Otherwise, set the computer_move to "unknown"

        if computer_symbol == 0
            computer_move = "rock"
        elsif computer_symbol == 1
            computer_move = "paper"
        elsif computer_symbol == 2
            computer_move = "scissors"
        else
            computer_move = "unknown"
        end

        # Step 5
        # Checking who wins
        if player_symbol > computer_symbol # player wins
            if computer_symbol == 0 && player_symbol == 2
                computer_score += 1
            else
                player_score += 1
            end

        ### ACTIVITY: ###
        # Complete the if-statement by checking if the computer wins using else-if
        # Else, print to the console: "It was a tie!"

        elsif computer_symbol > player_symbol # computer wins
            if player_symbol == 0 && computer_symbol == 2
                player_score += 1
            else
                computer_score += 1
            end
        else
            puts "It was a tie!"
        end

        # Step 6
        puts "The player's move was #{player_move} and the computer's move was #{computer_move}"
        puts "The player's score is #{player_score}"
        puts "The computer's score is #{computer_score}"
        
        # Step 7
        puts "Do you want to play again (Y or N)?"
        play_again = gets.chomp.upcase
        if play_again == 'N'
            play_again = false
            puts "\nGame has been terminated"
        else
            play_again = true
        end
    end
end

run_game()
