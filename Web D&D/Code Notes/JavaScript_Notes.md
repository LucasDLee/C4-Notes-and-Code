# JS Notes

Here, you'll find my notes regarding basic JS formatting. JS is the "behaviour" of our website. Just like a house electricity, plumbing and other aspects, so does a website and that website needs to use JS to make it interactive.

## Background Information

- JS stands for ***JavaScript***
- If you see `//`, that is a **comment**. Each coding language has their own form of comments and comments are used as notes to remind yourself (or your peers) what your code does.
- All JS files ends with ".js". Unlike an HTML file, you cannot open up a JS file normally.

## Using JS

### Connecting Your CSS File to Your HTML File

In the "head" of your HTML file, that is where we keep all of our information about our website such as the title and alphabet. We also want to connect any other files that our website might need (like CSS or JavaScript (JS) files). If we don't do that, the CSS we write won't show up on our website. We do that like so:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>My website</title>
        <meta charset="UTF-8">
        <script src="script.js"></script>
    </head>
</html>
```

- `script` refers to JavaScript. Unlike our CSS connection, we need to have both `<script>` and `</script>`
- `src` is the file's source or where it's located in our computer and `"script.js"` is the name of our JavaScript file

### Basic JavaScript

#### Data Types

In JavaScript, we need to store specific numbers, words, or other objects. We call these things **data types**. The most common data types are:

- Booleans (`true` or `false` values)
- Strings (words): All strings have quotation marks `""`
- Numbers
- Undefined

We also want to use something called `console.log()` to print out our values so we know what we're doing with them.

```js
    //'let' is the keyword to make a variable
    //'name' is the variable's name
    //'Lucas' is my data type associated with my variable name
    let name = "Lucas";
    console.log(name);

    //Strings (words)
    //All strings have quotation marks
    let bookTitle = "The Hobbit";
    console.log(bookTitle);

    //Numbers
    let age = 20;
    console.log(age);
    let old = age + 10;
    console.log(old);

    //Booleans (true or false variables)
    let isOpen = false;
    console.log(isOpen);
    isOpen = true;
    console.log(isOpen);

    //Connecting variables
    console.log("Age: " + age);

    console.log("Community " + "Centre");

    console.log(age + age); //40

    console.log("age + age"); //prints a word
```

##### Booleans

- They are either `true` or `false`
- You can print a boolean to the console like so: `console.log(true)` or `console.log(false)`
- We can also get booleans by comparing values
  - e.g. `console.log(3 > 1)` gives us `true`, a boolean

##### Strings

- All strings are within quotation marks ("insert your word here")
- If we want a string with nothing inside of it, just have the quotation marks ("")

##### Numbers

- You can use almost any number you want (-1, 100, 32432, -8832, etc.)
- If you type a really, really big number (e.g. 1000000000000000000), you will get "Infinity" instead of the number you put in

##### Undefined

- Denoted by `undefined` just like how we have `true` or `false` for booleans
- Useful when we want to assign a value to a variable but we don't know what it is yet

##### Arithmetic (math)

- Add: `+`
- Subtract: `-`
- Divide: `/`
- Multiply: `*`
- Modulo (remainder): `%`
  - Gets the remainder of a division statement
  - e.g. `3 % 2` gives me `1`

##### Comparison

- Greater than: `>`
- Greater than or equals to: `>=`
- Less than: `<`
- Less than or equals to: `<=`
- Check if 2 things are the same: `==`

>`==` is not the same thing as `=`. `==` tells us we are comparing two values to see if they are the same thing while `=` says two things are now the same thing

For example:

```js
    let name = "Lucas"
    let name2 = "Not Lucas"
    // The variable of "name" is assigned to the value of "Lucas" and "name2" is assigned to the value of "Not Lucas"

    console.log(name == name2) //false
    // Using ==, we check if the variables known as "name" and "name2" have the same value
```

##### Checking Multiple Comparisons

What if I wanted to check if `2 > 1` and `3 > 2` in the same line? We can do that with `&&` or `||`.

- `&&`: Both conditions must be true for operation to be true
- `||`: Only one of the conditions must be true for the operation to be true

Here's some sample code:

```js
    //Checking multiple conditions
    //&&: both conditions must be true for the operation to work
    //||: one of the conditions must be true for the operation to be true

    //Booleans
    console.log(true && false);
    console.log(true && true);
    console.log(true || false);

    //Numbers
    console.log(5 > 0 && 2 < 0);
    console.log(5 > 0 || 2 < 0);
```

### If-Statements

Sometimes, we want our code to only run depending on certain conditions. For example, if its rainy outside, we want to bring an umbrella. Using if-statements, we can simulate something like that. Here's some things we need:

- `if` keyword tells us we're using an if-statement
- Conditions found in round brackets `( )`
  - A **condition** is a comparison that needs to be checked
  - For this, we need to make a `true` or `false` statement through comparisons
- Curly brackets after our round brackets `{ }`
  - In between the 1st curly bracket `{` and the 2nd curly bracket is our code `}`
- `else if` keywords used in-case the `if` or `else-if` statement above it was false
  - Must always be put after an `if` statement
  - Follows the same format with brackets as an `if` statement
- `else` keyword is the default usage in case everything else fails
  - Always put at the end of an `if` statement
  - Does not need the round brackets

Here's an example of checking if a number is positive or negative, even or odd:

```js
    //If-statements
    //3 parts of an if-statement:
    //"if" keyword
    //conditions found in ( )
    //curly brackets where our code will be in { }
    let number = -3;

    if(number > 0) {
        console.log("This is a positive number");
        if(number % 2 == 0) {
            console.log("Even number");
        }
    } else if(number < 0) {
        console.log("This is a negative number");
        if(number % 2 == -1) {
            console.log("Odd number");
        }
    } else if(number == 0) {
        console.log("Zero");
    } else {
        console.log("idk");
    }
```

### Switch Statements

They have the same usage as if-statements but just are formatted differently. We also need to know a few things about switch-statements:

- `switch` keyword tells us we're making a switch-statement
- Round brackets with a parameter right after the `switch` keyword to check what's being looked at
- Curly brackets to hold the code. Within the curly brackets, we have the following:
  - `case`: Checks if our parameter matches our "case". Next to the `case` is what I want to look for
  - `break`: Put after the `case`'s code to prevent the switch-statement from continuing
  - `default`: Same thing as the `if` statement's `else`. Does not need the `break`.

Here's an example:

```js
    //Switch statements
    let day = "Monday";

    switch(day) {
        case "Monday":
            console.log("Today is Monday");
            break;
        default:
            console.log("Couldn't find any more days");
    }
```

### Loops

A loop is a coding mechanism in which you can repeat a task multiple times without having to rewrite it

#### For-Loop

- Start off with a “for” and have the parameters next to the loop like so: for(let i = 0; i < 5; i++)
- In the parameters, you need the following:
  - The starting condition: e.g. let i = 0;
  - The ending condition: e.g. i < 5;
  - The iteration count (how many times your starting condition will change for every loop): e.g. i++ which means “for every loop, the variable ‘i’ will increase by 1”
- Curly brackets `{ }` are followed after every loop
- Within the curly brackets is the code you want to write

Here's an example:

```js
    for(let i = 0; i < 10; i = i + 1) {
        console.log("This is a for-loop");
    }
```

#### While-Loop

- Start with a “while” and have your parameter
  - Your parameter is a specific condition such that the loop will continue while your parameter is true
  - E.g. while(minutes < 60) { minutes += 1; }

Here's an example:

```js
    let j = 0;
    while(j < 10) {
        console.log("This is loop number " + j);
        j++;
    }
```

#### Do-While Loop

- Basically the same thing as a while loop but its “do { } while(parameter)”

Here's an example:

```js
    let m = 0;
    do {
        console.log(m)
        m += 1;
    } while(m < 5)
```

#### Differences

- **for** - loops through a block of code a number of times
- **while** - loops through a block of code while a specified condition is true
- **do/while** - also loops through a block of code while a specified condition is true
- Also, a **while** loop will check the parameters first and then execute the code if it is true whereas a **do/while** loop will run the code first and then check if the parameters are true

### Functions

What is a function? A function is a piece of code we can pre-define so we can reuse it later.

- A block of code that is used for a specific task
  - Need the following:
    - "function" keyword
    - Function name: functionName
    - Parameter brackets: () (parenthesis)
    - Curly brackets for code { }
- A function must be called for it to run. This means that there must be a specific button or feature in your website that gets the function to compile its code
- Parameters in functions
  - These are the requirements we need for a function to run and parameters are written in the form of a variable name
  - E.g. function functionName(parameter);
  - Parameters can be used in numerous ways:
    - Solving a math problem using numbers
    - Getting someone’s name using strings
    - Answering questions using booleans
- Return
  - The "return" keyword can be used to end a function
  - Typically put at the end
  - Can return an operation, variable or a data type
    - E.g. return “word”, return true, return isDaytime;
  - Assigning a variable to a function can assign whatever return value that is in the function to the variable
    - let currentTime = getTime(120);

Here's an example:

```js
    //Functions
    //A function is a piece of our code we can reuse that'll do a certain thing such as using loops or printing our name to the console

    //3 things in a function:
    //"function" keyword
    //function name: always comes after the "function" keyword
    //parameters: variables that we need to make our function work
    function add(x, y) {
        console.log(x + y)
    }

    //Calling our function
    add(8, 6)
    add(30, 1)

    function printLocation() {
        console.log("City Centre Community Centre")
    }
    printLocation()

    function multiply(x, y) {
        return x * y
        //return: instead of printing a value to the console, we can give out a new value by returning something
    }

    let multipliedNumber = multiply(4, 5)
    console.log(multipliedNumber)
    multipliedNumber = 3
```

#### Calling a Function

When we want a function to run, we must "call" it. This means we need to write its name with the necessary parameters.

- Type the function name with the parameters (if it has no parameters, just have the parenthesis)
  - E.g. functionName() or functionName(parameter)
- We can call a function to the console by assigning a variable to it. If the function has any console.log code, then that code will be printed out

### Document Object Model (DOM)

The Document Object Model (DOM) is a way to connect our JavaScript code to our HTML page. This is quite useful as it provides a medium for our users to interact with our website instead of having to search for and look at the console.

One way to use the DOM is to make a button in HTML:

```html
  <button>This is a button</button>

  <!-- I can connect my button to JavaScript using "onclick" -->
  <!-- onclick: Looks for the function associated with it and runs the code -->

  <button onclick="myFunction()">Button 1</button>
  <p id="my-demo">Among Us</p>
```

Once we specify those IDs or onclicks, we can then go to JavaScript to write the proper code.

```js
  function myFunction() {
    let getDemoId = document.getElementById("my-demo")
    getDemoId.innerHTML = "We are using the Document Object Model to change this text with JavaScript!"
  }
```

Some notes:

- `document`: Refers to the HTML file that is connected to your JS file
- `getElementById("id here")`: Looks for that specific ID
- `innerHTML`: Changes the HTML that is displayed on your website.

When someone clicks on **Button 1**, the text that says *Among Us* will change to *We are using the Document Object Model to change this text with JavaScript!*

#### Event Listeners

An event listener is a part of the DOM that **waits for an action** like a click, scroll, or keyboard button to be pressed and activates its code once that action has occured.

Another way to connect a button to HTML is through its ID:

```html
  <button id="my-button">Button 2</button>
```

In some cases, this can be more secure as it doesn't explicitly display which code you want to run when the button is pressed.

```js
  let testAlert = document.getElementById("my-button")

  // Part of the DOM, they wait for a certain action on our website and react accordingly
  testAlert.addEventListener("click", function() {
    alert("You used an event listener to call a pop up!")
  })
```

Some notes:

- `addEventListener(action, your-function)`: A part of the DOM that waits until something happens and then runs the code for it
  - `action`: Anything your user does on the website (e.g. click, scroll, keyboard press, etc.)
  - `your-function`: Any function you write that contains the code you want to run. A function with no name is called an "anonymous function"
- `alert`: A pop up that displays a message of sorts

When someone clicks on **Button 2**, a pop up with the message *You used an event listener to call a pop up!* appears at the top of your website.
