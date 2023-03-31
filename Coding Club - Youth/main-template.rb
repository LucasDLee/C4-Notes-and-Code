### Class 1 ###
puts "\nClass 1"

# What is Ruby?
# Ruby is a high-level, object-oriented programming language heavily inspired by Python

# Use the # to make a comment. Comments are notes in our code to remember what we wrote

puts "Hello, World!" # notice it say Hello, world! in the black box called the console

# Data Types #
puts "\nData Types"

## Strings (words)
## Anything with quotation marks " "

puts "My name"
puts "This is a string"

## Numbers ##

puts 5 # int
puts 3.0 # float (decimals)

## Booleans (yes/no questions) ##

puts true
puts false
puts 5 > 2

## Connecting Stuff Together ##

puts "Community " + "Centre"
puts "September " + "2022"
puts "September " + 2022.to_s
## connecting strings and numbers gives an error so we need to convert the number to a string with "to_s"

# Variables (ways to store our strings/numbers/booleans) #

## All variables have a name and a value
## example: variable_name = value

puts "\nVariables"
my_name = "Lucas"
puts my_name # putsing the variable means I puts the value associated with it
my_name = "Lee" # change the value of our variable
puts my_name

# Snake Case is a type of variable naming style. All spaces are replaced with underlines and all words are in lowercase
# e.g. super_string, snake_case

### ACTIVITY: ###
# 1) Make a variable called my_school and set the value to whatever school you go to
# 2) Once you do that, puts the variable
my_school = "SFU"
puts my_school

# Math #
puts "\nMath"
puts 8 + 3
puts 8 - 3
puts 8 * 3
puts 8 / 3

# Checking individual conditions #
puts "\nComparisons"
puts 6 > 1 # true
puts 6 < 1 # false
puts 5 >= 5 # true
puts 5 <= 4 # false
puts 3 == 3 # true
# use == to check if 2 things are the same
# notice how your console says true or false. That happens because we're checking if something is bigger/smaller than something else and if we do/don't, we get a yes/no or true/false

# Checking multiple conditions #
puts "\nChecking Multiple Conditions"
## and: both conditions must be true for the operation to work
## or: one of the conditions must be true for the operation to be true

# Booleans
puts (true and false) # false
puts (true and true) # true
puts (true or false) # true

# Numbers
puts (5 > 0 and 2 < 0) # false
puts (5 > 0 or 2 < 0) # true

### ACTIVITY: ###
# 1. Make a variable called age and assign it your current age
# 2. Use puts to check if your age is greater than 16 and greater than or equal to 19 and puts out your result

age = 20
puts age > 16 and age >= 19

# Arrays (Data Type) #
## Used to store multiple values instead of just 1 value to a variable 
puts "\nArrays"

colours = ["blue", "red", "green"]
print colours, "\n"
puts colours # print each item separately to the console

# In a array, you can change the values and also have duplicate values
puts colours.length() # 3
puts colours[0]  # getting the 1st item of my array
puts colours[-1] # getting the last item of my array
puts colours[colours.length() - 1] # getting the last item of my array
colours[0] = "orange"
print colours, "\n"

# Combining two arrays
years = [2000, 2001, 2002]
years_and_colours = years + colours
print years_and_colours, "\n"

# Storing Multiple Data Types
person = ["Lucas", "Lee", 2002, true]
print person, "\n"
puts person




### Class 2 ###
puts "\nClass 2"
