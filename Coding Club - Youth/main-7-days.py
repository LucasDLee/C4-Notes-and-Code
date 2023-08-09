### Class 1 ###
print("\nClass 1\n")

# What is Python? 
# Python is an object-oriented programming language used Facebook, Google, Netflix, etc.

# Use the # to make a comment. Comments are notes in our code to remember what we wrote

print("Hello, World!") # notice it say Hello, world! in the black box called the console

# Primitive Data Types #

## Strings (words)
## Anything with quotation marks " "

print("\nData Types")
print("My name")
print("This is a string")

## Numbers

print(5) # int
print(3.0) # float (decimals)

## Booleans (yes/no questions)

print(True)
print(False)
print(5 > 2)

# Connecting Stuff Together

print("Community " + "Centre")
print("September, " + "2022")
# connecting strings and numbers gives an error

# Variables (ways to store our strings/numbers/booleans) #

# All variables have a name and a value
# example: variableName = value

print("\nVariables")
my_name = "Lucas"
print(my_name) # printing the variable means I print the value associated with it
my_name = "Lee" # change the value of our variable
print(my_name)

# Snake Case is a type of variable naming style. All spaces are replaced with underlines and all words are in lowercase
# e.g. super_string, snake_case

### ACTIVITY ###
# 1) Make a variable called school and set the value to whatever school you go to
# 2) Once you do that, print the variable
school = "SFU"
print(school)

# Math #
print("\nMath")
print(8 + 3)
print(8 - 3)
print(8 * 3)
print(8 / 3)

# Checking individual conditions #
print("\nComparisons")
print(6 > 1)
print(6 < 1)
print(5 >= 5)
print(5 <= 4)
print(3 == 3) # use == to check if 2 things are the same
# notice how your console says True or False. That happens because we're checking if something is bigger/smaller than something else and if we do/don't, we get a yes/no or True/False

# Checking multiple conditions #

# and: both conditions must be true for the operation to work
# or: one of the conditions must be true for the operation to be true

# Booleans
print(True and False)
print(True and True)
print(True or False)

# Numbers
print(5 > 0 and 2 < 0)
print(5 > 0 or 2 < 0)

### ACTIVITY ###
# 1. Make a variable called age and assign it your current age
# 2. Use print to check if your age is greater than 16 AND greater than or equal to 19 and print out your result (you should get false in your output)

age = 21
print(age > 16 and age >= 19)



### Class 2 ###
print("\nClass 2\n")


# Lists #

print("\nLists")
colours = ["blue", "red", "green"]
print(colours)
# In a list, you can change the values and also have duplicate values
print(len(colours))
print(colours[0]) # getting the 1st item of my list
print(colours[-1]) # getting the last item of my list
colours[0] = "orange"
print(colours)
colours.append("yellow") # adds item to the list
print(colours)

# Combining two lists
years = [2000, 2001, 2002]
years_and_colours = years + colours
print(years_and_colours)

### ACTIVITY ###

# 1) Make a list called my_hobbies consisting of at least 2 hobbies (e.g. gaming, exercise, community outreach, coding, etc.)
# 2) Print out your list
# 3) Add another hobby to your list and then print it out again
my_hobbies = ["cycling", "hiking"]
print(my_hobbies)
my_hobbies.append("video games")
print(my_hobbies)

# If-statements #
print("\nIf-statements")

# An if-statement checks if something is True, and if it is, then it will run a specific set of code

# All if-statements start with the "if" keyword
a = 5
b = 3

if a > b:
    print("a is bigger than b")

# NOTICE the indent: If you have too many, or too little, indents (tab button) then your Python code won't work

## Else-if ##

# In case the if-statement above it didn't work, we can use "elif" to check and run our backup code
# The "elif" keyword is always after the first if-statement, or another "elif" statement, and is optional

if a > b:
    print("a is bigger than b")
elif a < b:
    print("a is smaller than b")
elif a == b:
    print("a is b")

## Else ##

# If our if- and else-if statements all fail, we can use an "else" to run our default code
# The "else" keyword is always at the end of an if-statement and is optional

if a > b:
    print("a is bigger than b")
elif a < b:
    print("a is smaller than b")
elif a == b:
    print("a is b")
else:
    print("Game over")

### ACTIVITY ###

# 1) Make a variable called dice and assign it to any positive number
# 2) If dice is smaller than 5, print "Not quite"
# 3) Else if dice is smaller than 10, print "Halfway there"
# 4) Else if dice is smaller than 20, print "Almost there"
# 5) Else if dice is greater than or equal to 20, print "You win"
# 6) Else print "Help"

dice = 11

if dice < 5:
    print("Not quite")
elif dice < 10:
    print("Halfway there")
elif dice < 20:
    print("Almost there")
elif dice >= 20:
    print("You win")
else:
    print("Help")

# and/or in if-statements
if a == 2 and b == 3:
    print("a is 3 and b is 3")

if a == 2 or b == 3:
    print("a is 2 and b is 3")



### Class 3 ###
print("\nClass 3\n")

# Loops #

# A loop is a coding mechanism that lets us do certain things 
# with our code without having to retype it

# There are 2 types of loops: for and while loops

# while-loops
# A while-loop runs "while" a condition is true
# 1) A starting variable (usually a number)
# 2) "while" keyword
# 3) Ending condition
# 4) Code within the while loop
# 5) Some way to change our starting variable
print("\nWhile-Loops")
i = 0
while i < 10:
    print(i)
    i = i + 1

# We can also have while-loops in another while-loop
i = 0
j = 0
while i < 10:
    print("Start new loop #" + str(i))
    while j < 10:
        print(j)
        j = j + 1
    j = 0 # reset j
    i = i + 1 # increase i by 1

# Stopping a while-loop midway
i = 0
while i < 5:
    print(i)
    if i == 2:
        break # stops the while-loop
    i += 1

# Just like an if-statement, we can use "else" to do something after our loop runs
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Finished loop")

# for-loops
# A for-loop runs through a sequence of items
# 1) A starting variable (like a list)
# 2) "for" and "in" keywords
# 3) Code within the loop
print("\nFor-Loops")
cars = ["Ferrari", "Volvo", "Toyota", "Mercedes"]
for x in cars:
    print(x)

city = "Richmond"
for j in city:
    print(j)

# See the first while-loop we made on
# We can do the same thing with a for-loop using range()
for k in range(10):
    print(k)
# range(number) is just a sequence of numbers

for k in range(-5, 0): # can set a starting and ending parameter in range
    print(k)
    
for k in range(-5, 5, 2): # can set a starting (-5) and ending (5) parameter in range as well as an increment value (2)
    print(k)
else:
    print("Loop done")

### ACTIVITY ###

# Using the "cars" list we made earlier, make a while-loop (not a for-loop) and print every item in the cars list
# Some notes:
# - len(cars) is the size of your list
# - cars[0] is the beginning of your list
cars = ["Ferrari", "Volvo", "Toyota", "Mercedes"] # DON'T CHANGE THIS

i = 0
while i < len(cars):
    print(cars[i])
    i = i + 1



### Class 4 ###
print("\nClass 4\n")

# Functions #

# A function is a piece of code that we predefine so we can use it as many times as we want
# Math: y = mx + b, y = 4x

# 3 things to make a function:
# 1) "def" (define) keyword
# 2) The function's name
# 3) Round () brackets
# e.g. def myFunction()
print("\nFunctions")
def say_hi():
    print("Hi!")

# To make the function work, we need to write the function name and brackets
# This is called "calling a function"
say_hi()
say_hi()

# Sometimes, we have a function that takes argument(s)

def greeting(name):
    print("Hi, " + name + "!")
# An argument is some information needed to be put into the function so that it works
# greeting() # gives an error because its expecting 1 argument
greeting("Lucas")
greeting("Kasie")

# A function can take as many arguments as we want but for it to work,
# it needs the same amount of items put into those arguments

def add(x, y):
    print(x + y)

add(3, 5)
add(7, 20)

### ACTIVITY ###

# This activity involves "functions" and "loops"
# Your goal is to make a function that will repeat a specific statement for as many times as you tell it to

# 1) Make a function called "count_sheep". This function will take 1 argument called "number_of_sheep"
# 2) In your "count_sheep" function, make a for-loop that will run depending on how many sheep you input in "number_of_sheep"
#   2.1) e.g. if number_of_sheep is 3, your loop will run 3 times
#   2.2) e.g. if number_of_sheep is 2342, your loop will run 2342 times
# 3) In your for-loop, print to the console: "I have counted " + str(whatever your looping variable is) + " sheep"
#   3.1) e.g. if number_of_sheep is 3, you will see "I have counted 1 sheep", "I have counted 2 sheep", "I have counted 3 sheep"

# Loop for your function
# for x in range(1, number_of_sheep+1):
#     # more code in the loop

def count_sheep(number_of_sheep):
    for x in range(1, number_of_sheep+1):
        print("I have counted " + str(x) + " sheep")

count_sheep(7)

# When we make a function, sometimes it can "return" us the result
# This is useful as we can get very complicated calculations and by having "return" in a function
# allows us to do those calculations and associate them to some variable afterwards
# instead of putting all of those calculations on that variable

def divide(x, y):
    return x / y

divide(3, 4)
# Notice how nothing is printed here
# divide(3, 4) becomes 0.75
print(divide(3, 4))

get_divide_function_value = divide(5, 2)
print(get_divide_function_value)

### ACTIVITY ###

# In this activity, you will checking if the Pythagorean theorem is true/false for a triangle depending on the length of the sides you give it
# https://en.wikipedia.org/wiki/Pythagorean_theorem
# https://www.infoplease.com/math-science/mathematics/numbers-formulas/powers-and-exponents

# Steps:
# 1) Make a function called is_pythagorean with 3 arguments called x, y, and z
# 2) Return true if it satisfies the "Symbolic Statement" from the Wikipedia link and False if it doesn't

def is_pythagorean(x, y, z):
    return (
        (x*x) + (y*y) == (z*z)
    )

print(is_pythagorean(3, 4, 5)) # True
print(is_pythagorean(1, 1, 2)) # False
