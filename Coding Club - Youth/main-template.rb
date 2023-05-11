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

### ACTIVITY ###
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

### ACTIVITY ###
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

### ACTIVITY ###

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
if (a == 2 and b == 5)
    puts "a is 2 and b is 5"
end

if (a == 2 or b == 5)
    puts "a is 2 or b is 5"
end

### ACTIVITY ###

# 1. Make a variable called dice and assign it any positive number
# 2. If dice is smaller than 5, print "Not quite"
# 3. Else if dice is smaller than 10, print "Halfway there"
# 4. Else if dice is smaller than 20, print "Almost there"
# 5. Else if dice is greater than or equal to 20, print "You win"
# 6. If all of the if- and else-if statements fail, print "Help"

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
# 1) A starting variable (like an array)
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

### ACTIVITY ###

# Using the "cars" array we made earlier, do the following:
# Make a while-loop (not a for-loop) and print every item in the cars array individually
# Some notes:
# 1) cars.length() is the size of your array
# 2) cars[0] is the beginning of your array
cars = ["Ferrari", "Volvo", "Toyota", "Mercedes"]

i = 0
while i < cars.length()
    puts cars[i]
    i = i + 1
end

puts "\nClass 5"

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

### ACTIVITY ###
# Make an until loop that starts at 1 and runs until you find a number divisible by 13 (y % 13)
y = 1
until y % 13 == 0 do
    puts y
    y += 1
end


### Class 5 ###

# Functions #

# A function is a piece of code that we predefine so we can use it as many times as we want
# Math: y = mx + b, y = 4x

# 3 things to make a function:
# 1) "def" (define) keyword
# 2) The function's name
# 3) Round () brackets
# e.g. def myFunction()
puts "\nFunctions"
def say_hi
    puts "Hi!"
end

# To make the function work, we need to write the function name and brackets
# This is called "calling a function"
say_hi # Hi!
say_hi # Hi!

# Sometimes, we have a function that takes argument(s)

def greeting(name)
    puts "Hi " + name + "!"
end
# An argument is some information needed to be put into the function so that it works
# greeting() # gives an error because it's expecting 1 argument
greeting("Lucas") # Hi Lucas!
greeting("Kasie") # Hi Kasie!

# A function can take as many arguments as we want but for it to work,
# it needs the same amount of items put into those arguments

def add(x, y)
    puts x + y
end

add(3, 5)
add(7, 20)

### ACTIVITY ###

# This activity involves "functions" and "loops"
# Your goal is to make a function that will repeat a specific statement for as many times as you tell it to
# 1) Make a function called "count_sheep". This function will take 1 argument called "number_of_sheep"
# 2) In your "count_sheep" function, make a for-loop that will run depending on how many sheep you input in "number_of_sheep"
#   2.1) e.g. if number_of_sheep is 3, your loop will run 3 times
#   2.2) e.g. if number_of_sheep is 2342, your loop will run 2342 times
# 3) In your for-loop, print to the console: "I have counted " + whatever your looping variable is.to_s + " sheep"
#   3.1) e.g. if number_of_sheep is 3, you will see "I have counted 1 sheep", "I have counted 2 sheep", "I have counted 3 sheep"

def count_sheep(number_of_sheep)
    for x in 1..number_of_sheep
        puts "I have counted #{x} sheep"
    end
end

count_sheep(7)

# When we make a function, sometimes it can "return" us the result
# This is useful as we can get very complicated calculations and by having "return" in a function
# allows us to do those calculations and associate them to some variable afterwards
# instead of putting all of those calculations on that variable

def divide(x, y)
    return x.to_f / y.to_f
end
# to_f: Changes an integer to a decimal number

# Notice how nothing is printed here
# divide(3, 4) becomes 0.75
puts divide(3, 4) # 0.75
puts divide(5, 8) # 0.625

get_divide_function_value = divide(5, 2) # 2.5
puts get_divide_function_value

### ACTIVITY ###

# In this activity, you will checking if the Pythagorean theorem is true/false for a triangle depending on the length of the sides you give it
# https://en.wikipedia.org/wiki/Pythagorean_theorem

# Make a function called is_pythagorean with 3 arguments called x, y, and z
# Return true if x^2 + y^2 equals to z^2 and false if it doesn't

def is_pythagorean(x, y, z)
    return (((x*x) + (y*y)) == (z*z))
end

puts is_pythagorean(3, 4, 5) # true (because 3*3 + 4*4 == 5*5 results in 9 + 16 == 25 which is correct)
puts is_pythagorean(1, 1, 2) # false (because 1*1 + 1*1 == 2*2 results in 1 + 1 == 4 which isn't correct)



### Class 6 ###

# Arbritrary Arugments in Functions #

# Arbritrary argument (*my_argument): Used if you don't know how many arguments you want in your function

def my_students(*students)
    puts "I teach #{students[0]}, #{students[1]}, and #{students[2]}"
end

my_students("A", "B", "C")
my_students("A", "B", "C", "D") # notice how "D" isn't used here
# my_students("Abe", "Bob") # notice how we get an error because we expect 3 students to print out but only 2 are present

### ACTIVITY: ###

# In this activity, you'll be dealing with "arbritrary arguments" and "loops"
# Make a function called print_all_people with 1 arbritrary argument called people
# Using a loop, print every individual person in *people
# Note: Arbritrary arguments are ARRAYS
# e.g. *my_argument => my_argument = [a, b, c, d, ...]

def print_all_people(*people)
    for x in people
        puts x
    end
end

print_all_people("Haley", "Elaina", "Liwei", "Jimmy", "Ki Yi", "Kai", "Yubin", "Benson", "Stephen", "Toyota", "Bryan", "Daniel")

# Lambda Functions #

# An anonymous function (or a function with no name)
# Used for small calculations
# Format: lambda { |arguments| block }
# e.g. lambda { |x| x + 5 }
    # if x = 3, we return 8
    # if x = -7, we return 2

puts (lambda { |x| x + 5 }).call(3)

# call() assigns some value to your anonymous function

# You can assign Lambda Functions to variables
multiply = lambda { |x, y| x * y }
puts multiply.call(3, 5) # x = 3, y = 5, x * y => 15
puts multiply.call(8, 6) # x = 8, y = 6, x * y => 48

# Lambda Functions can also be in a regular function
def subtract(x)
    lambda { |y| x - y }
end

puts subtract(3).call(8) # x = 3, y = 8, x = y = -5
puts subtract(12).call(-7) # x = 12, y = -7, x - y = 19

### ACTIVITY ###

# This activity will involve "lambda functions"
# Your goal is to make a lambda function that has 1 argument called
# my_name and print out the saying "Hi, [my_name]!"

# TWO IMPORTANT NOTES:
# - This lambda function we are making is the SAME THING as the first non-lambda function we made called greeting(name)
# - Look at the `multiply = lambda { |x, y| x * y }` function to help you identify how a lambda function is formatted

# Instructions
# 1) Make a variable called new_greeting
# 2) Have new_greeting be equal to a lambda function that takes 1 argument of my_name
# 3) Print to the console: "Hi [my_name]!"

new_greeting = lambda { |my_name| puts "Hi #{my_name}!" }
new_greeting.call("Lucas") # Hi Lucas!
new_greeting.call("Kasie") # Hi Kasie!



### Class 7 ###
puts "\nClass 7\n"

# Classes #

# Ruby is what we call an Object-Oriented language. This means we get items like a person or a building, 
# get their main properties (hair colour, height, weight), and objectify them

# To make a class, we need the following:
# 1) "class" keyword
# 2) Class name (always start with a capital letter)

class Person
    attr_accessor :eye_colour, :hair_colour, :height, :is_employed
    def initialize
        @eye_colour = "Brown"
        @hair_colour = "Black"
        @height = 180
        @is_employed = true
    end
end

# Classes can be reused like functions and assigned to variables
# A new class can be made by writing the class name followed by round brackets
# e.g. ClassName()

p1 = Person.new
puts p1
puts p1.eye_colour
puts p1.height
puts p1.is_employed

# However, every Person is different. As such, when we make a class, we may want to "initialize" it
# When we make a new Person, we can input certain properties to create (or initialize) the class

class Person2
    attr_accessor :eye_colour, :hair_colour, :height, :is_employed
    def initialize(eC, hC, h, isEmp)
        @eye_colour = eC
        @hair_colour = hC
        @height = h
        @is_employed = isEmp
    end
end

# "self" refers to the Person2's template and how we can put things in that template to get unique Person2's

p2 = Person2.new("Blue", "Blonde", 200, true)
puts p2
puts p2.eye_colour
puts p2.height
puts p2.is_employed


# Notice how when we print p1 or p2 by itself, we get a weird message declaring the class name and a bunch of letters and numbers
# That is the class representation as a string
# Obviously, it doesn't look readable but using the to_s() function, we can format it better

class Person3
    attr_accessor :eye_colour, :hair_colour, :height, :is_employed
    def initialize(eC, hC, h, isEmp)
        @eye_colour = eC
        @hair_colour = hC
        @height = h
        @is_employed = isEmp
    end

    def to_s
        "Eye colour: #{@eye_colour}, hair colour: #{@hair_colour}, height: #{@height}"
    end
end

p3 = Person3.new("Blue", "Blonde", 200, true)
puts p3

# To delete a class, write "undef"
# undef p3
# puts p3 gives an error

# If we want to make a class with nothing in it, we can use "pass"

class Person4
end

### ACTIVITY: ###

# Build a new class based on your school:
# 1) Name your class School. This class will have both the initialize and to_s functions
# 2) Your class should have the variables of school_name as a string (word) and number_of_classrooms, teachers, and students are all numbers
# 3) In the to_s function, it should say school_name + " has " + number_of_classrooms.to_s + " classrooms, " + teachers.to_s + " teachers, and " + students.to_s + " students"
# 4) Make a new object of this newly built class with whatever values you want and print it out

class School
    def initialize(name, n_of_c, t, s)
        @school_name = name
        @number_of_classrooms = n_of_c
        @teachers = t
        @students = s
    end

    def to_s
        "#{@school_name} has #{@number_of_classrooms} classrooms, #{@teachers} teachers, and #{@students} students"
    end
end

puts School.new("McMath", 100, 6, 2343)
puts School.new("Burnett", 8, 435, 1)
