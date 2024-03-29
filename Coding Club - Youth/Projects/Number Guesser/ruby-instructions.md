# Ruby: Making a Number Guesser

## Description

In this final activity, you will be making a number guesser game where a user/player has to guess the number that is generated in your Python code.

Here's an example of what it should look like when you're done:

![example](snapshot.png)

## Step 1: Setting Up

Here, we need to make some starting variables and functions to build the structure of our game. Do the following:

1) Import the random library from Ruby by doing ``require 'securerandom'``. *Libraries* in coding/programming are a set of premade code to do a certain task. They are useful because we might not want to rewrite code that someone else has made so we can instead borrow it by using *require*
2) Make a function called ``run_game()``. Inside this function, make a variable called ``play_again`` which is ``true``. ``play_again`` will be used to ensure the game runs forever until you tell it to stop

Here's what the code should look like so far:

```ruby
    require 'securerandom'

    def run_game()
        play_again = true

    end

    run_game()
```

## Step 2: Making a While-loop

Now, to make our game run **forever** until we tell it to stop, we're going to have to use a while-loop that is connected to ``play_again``.

EVERYTHING we write from this point on will go inside of our ``run_game()`` function.

1) Make a ``while`` loop that runs while ``play_again`` is the same as ``true``
2) Inside your while-loop, make a variable called ``generate_number`` which is equal to ``SecureRandom.random_number(11)``. ``SecureRandom.random_number(11)`` gets a random number from 0 to 10 inclusive (0 <= number <= 10)

## Step 3: Asking for Your Guess

Once we've made our while-loop, we need to print to the console some words for our user to understand what is happening. **All of the code that we will now write goes inside the while-loop.**

1) Print (or ``puts``) to the console: "Guess a number between 0 and 10 inclusive!" with `\n` in front of the "G" in "Guess". `\n` makes a new line which helps with spacing issues
2) After that, make a variable called ``your_guess`` which is equal to ``gets.to_i``. This code takes what we call an ``gets`` which is any user's response. ``to_i`` changes our response to an number

## Step 4: Checking if You Won

Use an if-statement for this part. We need to let our user know if they won or lost.

1) If ``your_guess`` and ``generate_number`` are the same, print (or ``puts``) to the console: "You won! Your guess was " + str(your_guess) + " and so was the answer!"
2) Else, print (or puts) to the console: "You lost. Your guess was " + str(your_guess) + " and the number was " + str(generate_number)

## Step 5: Playing the Game Again

Here, we want to ask the user if they want to play again.

1) Print to the console: "Do you want to play again (Y or N)? "
2) Assign the ``play_again`` variable to equal an ``gets.chomp.upcase`` (see Step 3). This code takes what we call an ``gets`` which is any user's response. ``upcase`` changes our response from lowercase to uppercase
3) Make an if-statement after that:
    1) If ``play_again`` is equal to ``'N'``, then set ``play_again`` to be ``false``
    2) Else, set ``play_again`` to be ``true``

That's it! If you run your code, it should be quite similar to the example provided at the beginning of this document.
