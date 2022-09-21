### Lecture 1 ###

# What is Python? 
# Python is an object-oriented programming language used Facebook, Google, Netflix, etc.

# Use the # to make a comment. Comments are notes in our code to remember what we wrote

from cmath import sqrt


print("Hello, World!") # notice it say Hello, world! in the black box called the console

# Data Types

## Strings (words)
## Anything with quotation marks " "

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

# Variables (ways to store our strings/numbers/booleans)

# All variables have a name and a value
# example: variableName = value

myName = "Lucas"
print(myName) # printing the variable means I print the value associated with it
myName = "Lee" # change the value of our variable
print(myName)

### ACTIVITY: 
# Make a variable called school and set the value to whatever school you go to
# Once you do that, print the variable
school = "SFU"
print(school)

# Math
print(8 + 3)
print(8 - 3)
print(8 * 3)
print(8 / 3)

# Checking individual conditions
print(6 > 1)
print(6 < 1)
print(5 >= 5)
print(5 <= 4)
print(3 == 3) # use == to check if 2 things are the same
# notice how your console says True or False. That happens because we're checking if something is bigger/smaller than something else and if we do/don't, we get a yes/no or True/False

# Checking multiple conditions

# and: both conditions must be true for the operation to work
# or: one of the conditions must be true for the operation to be true

# Booleans
print(True and False)
print(True and True)
print(True or False)

# Numbers
print(5 > 0 and 2 < 0)
print(5 > 0 or 2 < 0)

### ACTIVITY:
# Make a variable called age and assign it your current age
# Check if your age is greater than 16 and greater than or equal to 19 and print out your result

age = 20
print(age > 16 and age >= 19)

# Lists

colours = ["blue", "red", "green"]
print(colours)
# In a list, you can change the values and also have duplicate values
print(len(colours))
print(colours[0]) # getting the 1st item of my list
print(colours[-1]) # getting the last item of my list
colours[0] = "orange"
print(colours)



### Lecture 2 ###

# Combining two lists
years = [2000, 2001, 2002]
yearsAndColours = years + colours
print(yearsAndColours)

# Dictionaries #

# A dictionary in Python holds what we call "key: value" pairs
# This means we have a key, a topic or category, like colour, age, weight, height, etc.
# Values are properties of a key: blue, 20, 50, 175

person = {
    "name": "Lucas",
    "age": 20,
    "isAlive": True
}

print(person) # print the entire dictionary of person

print(person["name"]) # print an aspect of a person
print(person.get("name")) # does the same thing

print(person.keys()) # gets all the keys
print(person.values()) # gets all the values

# Updating our values

person["name"] = "Lee" # change a value
# e.g. dictionary["key"] = "new value"
print(person)

person.update({"name": "Lucas"}) # can change a value in our dictionary
print(person)

# Adding a new key: value pair

person.update({"height": 175})
print(person)

# Removing a key

person.pop("height")
print(person)

### ACTIVITY: ###

# 1) Make a dictionary called school
# 2) Have the keys of name, population, and location
# 3) Name and location be strings and population is a number
# 4) You can make up your values
# 5) Print all of your keys and values
# 6) Update your school's name to something else and then print the school name only

school = {
    "name": "UBC",
    "population": 60000,
    "location": "vancouver"
}
print(school.keys())
print(school.values())
school.update({"name": "SFU"})
print(school["name"])

# If-statements #

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

### ACTIVITY: ###

# Make a variable called dice and assign it any positive number
# If dice is smaller than 5, print "Not quite"
# Else if dice is smaller than 10, print "Halfway there"
# Else if dice is smaller than 20, print "Almost there"
# Else if dice is greater than or equal to 20, print "You win"
# Else print "Help"

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



### Lecture 3 ###

# and/or in if-statements

if a == 2 and b == 3:
    print("a is 3 and b is 3")

if a == 2 or b == 3:
    print("a is 2 and b is 3")

# Loops #

# A loop is a coding mechanism that lets us do certain things 
# with our code without having to retype it

# There are 2 types of loops: for and while loops

# while-loops
# A while-loop runs "while" a condition if true
# 1) A starting variable (usually a number)
# 2) "while" keyword
# 3) Ending condition
# 4) Code within the while loop
# 5) Some way to change our starting variable

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
    print("Stopped loop")

# for-loops
# A for-loop runs through a sequence of items
# 1) A starting variable (like a list)
# 2) "for" and "in" keywords
# 3) Code within the loop

cars = ["Ferrari", "Volvo", "Toyota", "Mercedes"]
for x in cars:
    print(x)

city = "Richmond"
for j in city:
    print(j)

# See the first while-loop we made on line 249
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

### ACTIVITY: ###

# Using the "cars" list we made earlier, do the following:
# Make a while-loop (not a for-loop) and print every item in the cars list
# Some notes:
# 1) len(cars) is the size of your list
# 2) cars[0] is the beginning of your list

i = 0
while i < len(cars):
    print(cars[i])
    i = i + 1

# Functions #

# A function is a piece of code that we predefine so we can use it as many times as we want
# Math: y = mx + b, y = 4x

# 3 things to make a function:
# 1) "def" (define) keyword
# 2) The function's name
# 3) Round () brackets
# e.g. def myFunction()

def sayHi():
    print("Hi!")

# To make the function work, we need to write the function name and brackets
# This is called "calling a function"
sayHi()
sayHi()

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

### ACTIVITY: ###

# Make a function called daysGoneBy. This function will take 1 number as an argument. You may call your argument whatever you like
# Within the function, make a for-loop. This for-loop's ending condition will be your function's argument (use range() for this)
# Within the for-loop, print "It is day #" + str(your argument)
# Test the function by calling it and see if it prints the number of days that corresponds to the number in your called function

def daysGoneBy(days):
    for x in range(days):
        print("It is day #" + str(x))

daysGoneBy(7)

# Functions continued #

# When we make a function, sometimes it can "return" us the result
# This is useful as we can get very complicated calculations and by having "return" in a function
# allows us to do those calculations and associate them to some variable afterwards
# instead of putting all of those calculations on that variable

def divide(x, y):
    return x / y

divide(3, 4) # notice how nothing is printed here
print(divide(3, 4))

divideFunction = divide(5, 2)
print(divideFunction)



### Lecture 4 ###

