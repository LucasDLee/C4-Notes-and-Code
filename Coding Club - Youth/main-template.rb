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

## !: gives you the opposite boolean
puts !true # false
puts !false # true

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
puts my_name # puts-ing the variable means I puts the value associated with it
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




### Class 2 ###
puts "\nClass 2"

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
colours.push("yellow")
print colours, "\n"
colours.pop()
print colours, "\n"
colours.pop(2)
print colours, "\n"

# Combining two arrays
years = [2000, 2001, 2002]
years_and_colours = years + colours
print years_and_colours, "\n"

# Storing Multiple Data Types
person = ["Lucas", "Lee", 2002, true]
print person, "\n"
puts person


# Hashes (Data Type) #
puts "\nHashes"
## Used to store "key: value" pairs
## key: Special keywords, cannot be duplicated
## value: Items attached to our keys
## Similar to an array of variables
my_grocery_store = {"Bread" => 5, "Rice" => 4, "Meat" => 12, "Milk" => 5}
print my_grocery_store, "\n"
puts my_grocery_store # same as print in this case
puts my_grocery_store["Bread"] # 5
puts my_grocery_store["Meat"] # 12
puts my_grocery_store[5] # nothing happens

## Adding to Hash
my_grocery_store["Cocoa"] = false
puts my_grocery_store

## Deleting from Hash
my_grocery_store.delete("Bread")
puts my_grocery_store # no more Bread

## Hashes need to be in strings or symbols
Orange = "orange"
my_grocery_store[Orange] = 67
puts my_grocery_store # error

## Keys and Values of Hashes
print my_grocery_store.keys, "\n"
print my_grocery_store.values, "\n"

### ACTIVITY: ###

# 1) Make a hash called my_school
# 2) In your hash, have the keys of name, population, and location. This refers to your school name, how many people are in your school, and where your school is located respectively
# 3) Assign values attached to your keys. You can just make up random values if you want
# 4) Print your keys in one line and your values in another line
# 5) Update your school's name to something else and then print the school name only
my_school = {"name" => "SFU", "population" => 30000, "location" => "burnaby"}
print my_school.keys, "\n"
print my_school.values, "\n"
my_school["name"] = "bcit"
puts my_school["name"]
my_school = {"Name" => "SFU", :pop => 30000, "Location": "Burnaby"}
puts my_school




### Class 3 ###
puts "\nClass 3"

# Symbols (Data Type) #
## Alternative keys in Ruby
puts "\nSymbols"

my_electronics_store = {:tv => "Television", :pc => "Personal Computer"}
puts my_electronics_store
puts my_electronics_store[:tv]
my_electronics_store[:ms] = "Microsoft" # add Microsoft to the store
puts my_electronics_store
my_electronics_store.delete(:pc) # delete Personal Computer
puts my_electronics_store

# The difference between Strings and Symbols is that Symbols take up less memory space and have better performance. We won't worry about this though


# If-statements #
puts "\nIf-statements"

# An if-statement checks if something is true, and if it is, then it will run a specific set of code

# All if-statements start with the "if" keyword
a = 5
b = 3

if a > b
    puts "a is bigger than b"
end # needed when we finish an if-statement

## Else-if ##

# In case the if-statement above it didn't work, we can use "elsif" to check and run our backup code
# The "elsif" keyword is always after the first if-statement, or another "elsif" statement, and is optional

if a > b
    puts "a is bigger than b"
elsif a < b
    puts "a is smaller than b"
elsif a == b
    puts "a is b"
end

## Else ##

# If our if- and else-if statements all fail, we can use an "else" to run our default code
# The "else" keyword is always at the end of an if-statement and is optional

if a > b
    puts "a is bigger than b"
elsif a < b
    puts "a is smaller than b"
elsif a == b
    puts "a is b"
else
    puts "Game over"
end

# and/or in if-statements
if (a == 2 && b == 5)
    puts "a is 2 and b is 5"
end

if (a == 2 || b == 5)
    puts "a is 2 or b is 5"
end

### ACTIVITY: ###

# 1 Make a variable called dice and assign it any positive number
# 2 If dice is smaller than 5, print "Not quite"
# 3 Else if dice is smaller than 10, print "Halfway there"
# 4 Else if dice is smaller than 20, print "Almost there"
# 5 Else if dice is greater than or equal to 20, print "You win"
# 6 Else print "Help"

dice = 11

if dice < 5
    puts "Not quite"
elsif dice < 10
    puts "Halfway there"
elsif dice < 20
    puts "Almost there"
elsif dice >= 20
    puts "You win"
else
    puts "Help"
end




### Class 4 ###
puts "\nClass 4"

# Loops #

# A loop is a coding mechanism that lets us do certain things 
# with our code without having to retype it

# There are 4 types of loops: for, while, do while, and until loops

# while-loops
# A while-loop runs "while" a condition is true
# 1) A starting variable (usually a number)
# 2) "while" keyword
# 3) Ending condition
# 4) Code within the while loop
# 5) Some way to change our starting variable
puts "\nWhile-Loops"
i = 0
while i < 10
    puts i
    i = i + 1 # increase the loop by 1 everytime it runs
end

# We can also have while-loops in another while-loop
i = 0
j = 0
while i < 10
    puts "Start new loop #" + i.to_s
    while j < 10
        puts j
        j = j + 1
    end
    j = 0 # reset j
    i = i + 1 # increase i by 1
end

# Stopping a while-loop midway
i = 0
while i < 5
    puts i
    if i == 2
        break # stops the while-loop
    end
    i += 1
end

# for-loops
# A for-loop runs through a sequence of items and can also act like a while loop
# 1) A starting variable (like a list)
# 2) "for" and "in" keywords
# 3) Code within the loop
puts "\nFor-Loops"
cars = ["Ferrari", "Volvo", "Toyota", "Mercedes"]
for x in cars
    puts x
end

city = "Richmond"
for j in city.chars
    puts j
end

# See the first while-loop we made on
# We can do the same thing with a for-loop by specifying a specific set of numbers to go through
for k in 0...10 # ... means exclusive range, whereas .. means inclusive range
    puts k
end

for k in -5..0
    puts k
end

for k in (-5..5).step(2)
    puts k
end

### ACTIVITY: ###

# Using the "cars" list we made earlier, do the following:
# Make a while-loop (not a for-loop) and print every item in the cars list
# Some notes:
# 1) cars.length() is the size of your list
# 2) cars[0] is the beginning of your list
cars = ["Ferrari", "Volvo", "Toyota", "Mercedes"]

i = 0
while i < cars.length()
    puts cars[i]
    i = i + 1
end

# do while loops
puts "\ndo..while loops"
i = 0
loop do
    puts cars[i]
    if cars[i] == "Toyota"
        break
    end
    i += 1
end

# until loops
puts "\nuntil loops"
x = 0
until x == 6 do
    puts x*x
    x += 1
end
