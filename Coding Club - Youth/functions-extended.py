# Arbritrary Arugments in Functions #

# Arbritrary argument (*my_argument): Used if you don't know how many arguments you want in your function

def my_students(*students):
    print("I teach " + students[0] + ", " + students[1] + ", and " + students[2])

my_students("Abe", "Bob", "Carrey")
my_students("Abe", "Bob", "Carrey", "Deanna") # notice how "Deanna" isn't used here
# my_students("Abe", "Bob") # notice how we get an error because we expect 3 students to print out but only 2 are present

### ACTIVITY ###

# In this activity, you'll be dealing with "arbritrary arguments" and "loops"
# Make a function called print_all_people with 1 arbritrary argument called people
# Using a loop, print every individual person in *people
# Note: Arbritrary arguments are LISTS
#       e.g. *my_argument => my_argument = [a, b, c, d, ...]

def print_all_people(*people):
    for x in people:
        print(x)

print_all_people("Rovan", "Mikko", "Rex", "Oceania", "Kaylie", "Itamar", "Amanda", "Andy", "Elaina", "Sarah", "William", "Haoxuan")

# Lambda Functions #

# An anonymous function (or a function with no name)
# Used for small calculations
# Format: lambda [arguments] : [return expression]
# e.g. lambda x : x + 5
    # if x = 3, we return 8
    # if x = -7, we return 2
print((lambda x : x + 5)(3))

# def multiply(x, y):
#     return x * y

# You can attach Lambda Functions to variables
multiply = lambda x, y : x * y
print(multiply(3, 5)) # 15
print(multiply(8, 6)) # 48

# Lambda Functions can also be in a regular function
def subtract(x):
    return lambda y : x - y

print(subtract(3)(8)) # 3 - 8 = -5, x = 3, y = 8
print(subtract(12)(-7)) # 12 - -7 = 19, x = 12, y = -7

### ACTIVITY ###

# This activity will involve "lambda functions"
# Your goal is to make a lambda function that has 1 argument called
# my_name and print out the saying "Hi, [my_name]!"
# 1) Make a variable called new_greeting
# 2) Have new_greeting be equal to a lambda function that takes 1 argument of my_name
# 3) Print to the console: "Hi, [my_name]!"

new_greeting = lambda my_name : print("Hi,", my_name, "!")
new_greeting("Lucas") # Hi, Lucas!
new_greeting("Kasie") # Hi, Kasie!
