import random

def run_game():
    play_again = True

    while play_again == True:
        generate_number = random.randint(0,10) # 0, 1, 2, ..., 10
        print("\nGuess a number between 0 and 10 inclusive!")
        your_guess = int(input("What is your guess? "))

        if your_guess == generate_number:
            print("You won! Your guess was " + str(your_guess) + " and so was the answer!")
        else:
            print("You lost. Your guess was " + str(your_guess) + " and the number was " + str(generate_number))
        
        play_again = str(input("Do you want to play again (Y or N)? ")).upper()

        if play_again == 'N':
            play_again = False
        else:
            play_again = True

run_game()