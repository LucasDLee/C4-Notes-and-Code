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

# Pascal Case is a type of variable naming style. All spaces are replaced with underlines and all words are in lowercase
# e.g. super_string, pascal_case

### ACTIVITY: ###
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

### ACTIVITY: ###
# 1. Make a variable called age and assign it your current age
# 2. Use print to check if your age is greater than 16 and greater than or equal to 19 and print out your result

age = 20
print(age > 16 and age >= 19)

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

# Combining two lists
years = [2000, 2001, 2002]
years_and_colours = years + colours
print(years_and_colours)




### Class 2 ###
print("\nClass 2\n")

# Dictionaries #

# A dictionary in Python holds what we call "key: value" pairs
# This means we have a key, a topic or category, like colour, age, weight, height, etc.
# Values are properties of a key: blue, 20, 50, 175
print("\nDictionaries")
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

### ACTIVITY: ###

# 1) Make a variable called dice and assign it any positive number
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




### Class 3 ###
print("\nClass 3\n")

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



# Class 4 #
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

### ACTIVITY: ###

# This activity involves "functions" and "loops"
# 1) Make a function called "count_sheep". This function will take 1 argument called "number_of_sheep"
# 2) In your "count_sheep" function, make a for-loop that will run depending on how many sheep you input in "number_of_sheep"
#   2.1) Use "range" for your ending condition
			# 2.1.1) "range" goes through a sequence of numbers
			# 2.1.2) e.g. range(6) gives us 0, 1, 2, 3, 4, 5
#   2.2) e.g. if number_of_sheep is 3, your loop will run 3 times
#   2.3) e.g. if number_of_sheep is 2342, your loop will run 2342 times
# 3) In your for-loop, print to the console: "I have counted " + str(number_of_sheep) + " sheep"
#   3.1) e.g. if number_of_sheep is 3, you will see "I have counted 1 sheep", "I have counted 2 sheep", "I have counted 3 sheep"

def count_sheep(number_of_sheep):
    for x in range(number_of_sheep):
        print("I have counted " + str(x) + " sheep")


# Functions continued #

# When we make a function, sometimes it can "return" us the result
# This is useful as we can get very complicated calculations and by having "return" in a function
# allows us to do those calculations and associate them to some variable afterwards
# instead of putting all of those calculations on that variable

def divide(x, y):
    return x / y

divide(3, 4) # notice how nothing is printed here
print(divide(3, 4))

get_divide_function_value = divide(5, 2)
print(get_divide_function_value)

# Arbritrary Arugments in Functions

# Arbritrary argument (*): Used if you don't know how many arguments you want in your function

def my_students(*students):
    print("I teach " + students[0] + ", " + students[1] + ", and " + students[2])

my_students("Abe", "Bob", "Carrey")
my_students("Abe", "Bob", "Carrey", "Deanna") # notice how "Deanna" isn't used here
# my_students("Abe", "Bob") # notice how we get an error because we expect 3 students to print out but only 2 are present

# Classes #

# Python is what we call an Object-Oriented language. This means we get items like a person or a building, 
# get their main properties (hair colour, height, weight), and objectify them

# To make a class, we need the following:
# 1) "class" keyword
# 2) Class name (always start with a capital letter)

class Person:
    eye_colour = "Brown"
    hair_colour = "Black"
    height = 180
    is_employed = True

# Classes can be reused like functions and assigned to variables
# A new class can be made by writing the class name followed by round brackets
# e.g. ClassName()

p1 = Person()
print(p1)
print(p1.eye_colour)
print(p1.height)
print(p1.is_employed)

# However, every Person is different. As such, when we make a class, we may want to "initialize" it
# When we make a new Person, we can input certain properties to create (or initialize) the class

class Person2:
    def __init__(self, eC, hC, h, isEmp):
        self.eye_colour = eC
        self.hair_colour = hC
        self.height = h
        self.is_employed = isEmp
# "self" refers to the Person2's template and how we can put things in that template to get unique Person2's

p2 = Person2("Blue", "Blonde", 200, True)
print(p2)
print(p2.eye_colour)
print(p2.height)
print(p2.is_employed)



# Class 5 #

# Classes continued #

# Notice how when we print p1 or p2 by itself, we get a weird message declaring the class name and a bunch of letters and numbers
# That is the class representation as a string
# Obviously, it doesn't look readable but using the __str__() function, we can format it better

class Person3:
    def __init__(self, eC, hC, h, isEmp):
        self.eye_colour = eC
        self.hair_colour = hC
        self.height = h
        self.is_employed = isEmp

    def __str__(self):
        return ("Eye colour: " + self.eye_colour + ", hair colour: " + self.hair_colour + ", height: " + str(self.height))

p3 = Person3("Blue", "Blonde", 200, True)
print(p3)

# To delete a class, write "del"
del p3
# print(p3) gives an error

# If we want to make a class with nothing in it, we can use "pass"

class Person4:
    pass

### ACTIVITY: ###

# Build a new class based on your school:
# 1) Name your class School. This class will have both the __init__() and __str__() functions
# 2) Your class should have the variables of schoolName as a string (word) and numberOfClassrooms, teachers, and students are all numbers
# 3) In the __str__() function, it should say schoolName + " has " + numberOfClassrooms + " classrooms, " + teachers + " teachers, and " + students + " students"
    # 3.1) REMEMBER TO CONVERT INTS TO STRINGS by doing str(345) => "345"
# 4) Make a new object of this newly built class with whatever values you want and print it out

class School:
    def __init__(self, name, nOfC, t, s):
        self.schoolName = name
        self.numberOfClassrooms = nOfC
        self.teachers = t
        self.students = s
    
    def __str__(self):
        return (self.schoolName + " has " + str(self.numberOfClassrooms) + " classrooms, " + str(self.teachers) + " teachers, and " + str(self.students) + " students")

print(School("McMath", 100, 6, 2343))
print(School("Burnett", 8, 435, 1))

# Inheritance: Classes continued #

# It is when one class is a part of, or depends on, another class

# 1) Parent class: Class being inherited from
# 2) Child class: Part of another class (Child depends on Parent)

class Person5:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def __str__(self):
        return (self.firstName + " " + self.lastName)

class Student(Person5): # Student depends on Person5
    def __init__(self, fname, lname, gr, studNum):
        Person5.__init__(self, fname, lname)
        # super().__init__(self, eC, hC, h, isEmp) does the same thing as above
        self.grade = gr
        self.studentNumber = studNum

s1 = Student("Joe", "Obama", 3, 123)
print(s1) # Notice how it prints the full name. That's because its take the __str__ function from its parent's class

class Student2(Person5):
    def __init__(self, fname, lname, gr, studNum):
        Person5.__init__(self, fname, lname)
        # super().__init__(self, eC, hC, h, isEmp) does the same thing as above
        self.grade = gr
        self.studentNumber = studNum

    # We can either explicitly tell our code to take the __str__ function from the Parent class
    # or we can make our own
    def __str__(self):
        # return super().__str__()
        return (super().__str__() + " is in grade " + str(self.grade) + " with student #" + str(self.studentNumber))
        # IF we want something from our parent's class, just write self.variableName

s2 = Student2("Joe", "Obama", 3, 123)
print(s2)

### ACTIVITY: ###

# Using the School class you made in the previous activity, make a Classroom that inherits from School:
# 1) The Classroom class should have both __init__() and __str__() functions
# 2) Every classroom should have the variables of capacity (number), roomNumber (number), floorNumber (number), and isOccupied (boolean)
# 3) The __str__() function should return "Classroom #" + self.roomNumber + " is on floor " + self.floorNumber + " at " + self.schoolName
# 4) Make a new object of Classroom and print it out

class Classroom(School):
    def __init__(self, name, nOfC, t, s, capacity, rN, fN, iO):
        super().__init__(name, nOfC, t, s)
        self.capacity = capacity
        self.roomNumber = rN
        self.floorNumber = fN
        self.isOccupied = iO

    def __str__(self):
        return ("Classroom #" + str(self.roomNumber) + " is on floor " + str(self.floorNumber) + " at " + self.schoolName)


c1 = Classroom("McMath", 100, 6, 2343, 20, 1, 2, True)
print(c1)