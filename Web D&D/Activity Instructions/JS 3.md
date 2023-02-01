# Activity Instructions

## JavaScript Loops and Functions

Using functions in JavaScript, do the following:

1) Part 1:
    1) Make a function called ``greeting(your parameters go here)``. This function will take one parameter called ``yourName``
    2) In your function, make a for-loop that **starts at 0**, **ends at 10 (less than 10)**, and **increases by 1** every time the loop runs
    3) In your loop, print to the console "Hello, my name is " + ``yourName``
    4) Outside of your function, write the following: ``greeting("ThisName")``. Replace *ThisName* with your actual name. You should see it say "Hello, my name is [yourName]" 10 times
2) Part 2:
    1) Make a function called "pythagorean" with 3 parameters called ``x``, ``y``, and ``z``
    2) To calculate the sides of a right triangle, we use the [Pythagorean Theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem) which states x&#178; + y&#178; = z&#178;
    3) In our function, **return true** if x&#178; + y&#178; = z&#178; and **return false** if x&#178; + y&#178; &#8800; z&#178;. To get something like x&#178;, you can do **x * x**
    4) Finally, write ``console.log(pythagorean(3, 4, 5))`` outside of your function. You should see it say ``true``