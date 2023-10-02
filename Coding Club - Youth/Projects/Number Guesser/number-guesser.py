# Step 1
import random

def run_game():
    play_again = True

    # Step 2
    while play_again == True:
        generate_number = random.randint(0,10) # 0, 1, 2, ..., 10
        
        # Step 3
        print("\nGuess a number between 0 and 10 inclusive!")
        your_guess = int(input("What is your guess? "))

        # Step 4
        if your_guess == generate_number:
            print("You won! Your guess was " + str(your_guess) + " and so was the answer!")
        else:
            print("You lost. Your guess was " + str(your_guess) + " and the number was " + str(generate_number))

        # Step 5 
        play_again = str(input("Do you want to play again (Y or N)? ")).upper()

        if play_again == 'N':
            play_again = False
        else:
            play_again = True

# run_game()

# Step 6
import tkinter as tk

game = tk.Tk()
game.title("Number Guesser")

explanation = tk.Label(
    text="Guess a number between 0 and 10 inclusive!"
).pack()
input_explanation = tk.Label(
    text="What is your guess?"
).pack()
result = tk.Label()
result.pack()

user_input = tk.Entry()
user_input.pack()

# Step 7
def run_game2():
    generate_number = random.randint(0,10) # 0, 1, 2, ..., 10
    
    your_guess = int(user_input.get())
    
    if your_guess == generate_number:
        result.config(text="You won! Your guess was " + str(your_guess) + " and so was the answer!")
    else:
        result.config(text="You lost. Your guess was " + str(your_guess) + " and the number was " + str(generate_number))

run_game = tk.Button(
    text="Submit",
    command=run_game2
).pack()


game.mainloop()
