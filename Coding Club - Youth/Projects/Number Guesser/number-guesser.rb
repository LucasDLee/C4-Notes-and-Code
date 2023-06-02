# Step 1
require 'securerandom'

def run_game()
    play_again = true

    # Step 2
    while play_again == true
        generate_number = SecureRandom.random_number(11) # 0, 1, 2, ..., 10
        
        # Step 3
        puts "\nGuess a number between 0 and 10 inclusive!"
        your_guess = gets.to_i

        # Step 4
        if your_guess == generate_number
            puts "You won! Your guess was #{your_guess} and so was the answer!"
        else
            puts "You lost. Your guess was #{your_guess} and the number was #{generate_number}"
        end

        # Step 5
        print "Do you want to play again (Y or N)? "
        play_again = gets.chomp.upcase

        if play_again == 'N'
            play_again = false
        else
            play_again = true
        end
    end
end

run_game()
