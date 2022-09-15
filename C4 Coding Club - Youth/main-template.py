### Lecture 1 ###

# What is Python? 
# Python is an object-oriented programming language used Facebook, Google, Netflix, etc.

# Use the # to make a comment. Comments are notes in our code to remember what we wrote

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

# Make a dictionary called school
# Have the keys of name, population, and location
# Name and location must be strings. Population is a number
# You can make up your values
# Print all of your keys and values
# Update your school's name to something else and then print the school name only

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

# and/or in if-statements

if a == 2 and b == 3:
    print("a is 3 and b is 3")

if a == 2 or b == 3:
    print("a is 2 and b is 3")



### Lecture 3 ###

# Loops #

# There are 2 types of loops: for and while loops

# while-loops ##
