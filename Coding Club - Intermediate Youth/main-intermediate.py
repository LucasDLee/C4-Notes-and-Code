### Class 1 ###
print("\nClass 1\n")

# Classes #

# Python is what we call an Object-Oriented language. This means we get items like a Vehicle or a building, 
# get their main properties (hair colour, height, weight), and objectify them

# To make a class, we need the following:
# 1) "class" keyword
# 2) Class name (always start with a capital letter)

class Vehicle:
    brand = "Porche"
    colour = "Blue"
    has_bluetooth = True
    num_of_wheels = 2
    owner = "Lucas"

# Classes can be reused like functions and assigned to variables
# A new class can be made by writing the class name followed by round brackets
# e.g. ClassName()

v1 = Vehicle()
print(v1)
print(v1.colour)
print(v1.has_bluetooth)
print(v1.num_of_wheels)

# However, every Vehicle is different. As such, when we make a class, we may want to "initialize" it
# When we make a new Vehicle, we can input certain properties to create (or initialize) the class

class Vehicle2:
    def __init__(self, b, c, bt, w, o):
        self.brand = b
        self.colour = c
        self.has_bluetooth = bt
        self.num_of_wheels = w
        self.owner = o
# "self" refers to the Vehicle2's template and how we can put things in that template to get unique Vehicle2's

v2 = Vehicle2("Ferrari", "Aqua", False, 3, "Ruby")
print(v2)
print(v2.colour)
print(v2.has_bluetooth)
print(v2.num_of_wheels)

# Notice how when we print v1 or v2 by itself, we get a weird message declaring the class name and a bunch of letters and numbers
# That is the class representation as a string
# Obviously, it doesn't look readable but using the __str__() function, we can format it better

class Vehicle3:
    def __init__(self, b, c, bt, w, o):
        self.brand = b
        self.colour = c
        self.has_bluetooth = bt
        self.num_of_wheels = w
        self.owner = o

    def __str__(self):
        return (self.owner + " owns a " + self.colour + " " + self.brand + " with " + str(self.num_of_wheels) + " wheels")

v3 = Vehicle3("Honda", "Yellow", False, 5, "Joe")
print(v3)

# To delete a class, write "del"
del v3
# print(v3) gives an error

# If we want to make a class with nothing in it, we can use "pass"

class Vehicle4:
    pass

### ACTIVITY: ###

# Build a new class based on your fictional city:
# 1) Name your class MyCity. This class will have both the __init__() and __str__() functions
# 2) You should have the following variables: city_name, population, gdp, has_costco
    # 2.1) city_name is a string
    # 2.2) population and gdp are numbers
    # 2.3) has_costco is a boolean
# 3) In the __str__() function, it should print: [city name] has [population] people with a GDP of [gdp]. Also, Costco is [has costco]
    # 3.1) REMEMBER TO CONVERT INTS TO STRINGS by doing str(345) => "345"
# 4) Make a new object of this newly built class with whatever values you want and print it out

class MyCity:
    def __init__(self, c, p, g, hc):
        self.city_name = c
        self.population = p
        self.gdp = g
        self.has_costco = hc
    
    def __str__(self):
        return (self.city_name + " has " + str(self.population) + " people with a GDP of " + str(self.gdp) + ". Also, Costco is " + str(self.has_costco))

print(MyCity("Funky Town", 100, 6, True))
print(MyCity("Atlantis", 8, 435, False))



### Class 2 ###
print("\nClass 2\n")

# Inheritance #
# It is when one class is a part of, or depends on, another class

# 1) Parent class: Class being inherited from
# 2) Child class: Part of another class (Child depends on Parent)

class Vehicle5:
    def __init__(self, b, c, w):
        self.brand = b
        self.colour = c
        self.wheels = w

    def __str__(self):
        return ("A " + self.brand + ", " + self.colour + " vehicle with " + str(self.wheels) + " wheels")

class Car(Vehicle5): # Car depends on Vehicle5
    def __init__(self, b, c, w, s):
        Vehicle5.__init__(self, b, c, w)
        # super().__init__(self, eC, hC, h, isEmp) does the same thing as above
        self.seats = s

c1 = Car("Ferrari", "Black", 3, 9)
print(c1)
# Notice how it prints "A Ferrari, black vehicle with 3 wheels"
# The Car class takes the __str__() function from its parent

class Car2(Vehicle5): # Car depends on Vehicle5
    def __init__(self, b, c, w, s):
        Vehicle5.__init__(self, b, c, w)
        self.seats = s
    
    # We can either explicitly tell our code to take the __str__ function from the Parent class
    # or we can make our own
    def __str__(self):
        return ("A " + self.brand + ", " + self.colour + " vehicle with " + str(self.wheels) + " wheels and " + str(self.seats) + " seats")
        # IF we want something from our parent's class, just write self.variableName


c2 = Car2("Ford", "Brown", 34, 123)
print(c2)

### ACTIVITY: ###

# Using the MyCity class you made in the previous activity, make a MyStore class that inherits from MyCity:
# 1) The MyStore class should have both __init__() and __str__() functions
# 2) Every MyStore should have variables of store_name (string), date_established (number), and is_open (boolean)
# 3) In the __str__() function, it should print: [store_name] is in [city_name] and was established in [date_established]. 
# 4) Make a new object of MyStore and print it out
# 5) Finally, make a function called check_if_open(self) in MyStore that returns is_open
    # 5.1) Write print([class of MyStore].check_if_open()) to see your output

class MyStore(MyCity):
    def __init__(self, c, p, g, hc, sN, dE, iO):
        super().__init__(c, p, g, hc)
        self.store_name = sN
        self.date_established = dE
        self.is_open = iO

    def __str__(self):
        return (self.store_name + " is in " + self.city_name + " and was established in " + str(self.date_established))

    def check_if_open(self):
        return self.is_open


store1 = MyStore("Vulcan", 1, 6, 2343, "Walmart", 1900, False)
print(store1)
print(store1.check_if_open())


### Class 3 ###

# Exception Handling #

# Sometimes, we try to do things that aren't allowed and that crashes our code
# With Exceptions, we can "catch" those problems and tell it to do something else that won't crash our program
# https://docs.python.org/3/library/exceptions.html

# def divide(x, y):
#     return x / y

# print(divide(1, 0)) # gives ZeroDivisionError

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "You tried to divide by 0"
    except:
        return "IDK"

print(divide(1, 0)) # gives ZeroDivisionError
print(divide(1, 2)) # 0.5

### ACTIVITY ###
# Make a function that tries to subtract 2 numbers
# 1) The function's name will be called "subtract" with 2 arguments of x and y
#   1.1) If everything is all good, return the product of x and y
# 2) Use an exception that catches a TypeError if you don't input a number
#   2.1) If you catch this exception, return "You must subtract 2 numbers"

def subtract(x, y):
    try:
        return x - y
    except TypeError:
        return "You must subtract 2 numbers"

print(subtract(3, 9)) # -6
print(subtract("d", 35)) # You must subtract 2 numbers

# Scopes #
# Sometimes when we're coding, we might have variables with the same name (e.g. 2 variables called "x") in different parts of our code (e.g. "x" in a loop and "x" in a function)
# However, which variable (e.g. "x") are we really using?

# Local Scopes
# When our variable is found inside a function

def print_name():
    j = "Lucas" # local variable is "j"
    print(j)

print_name()

# Global Scopes

j = "Lee"

def print_name2():
    j = "Lucas"
    print(j)

print(j) # Lee
print_name2() # Lucas

# "global" keyword: Gets the variable with the same name OUTSIDE of our function

j = "Lee" # global variable

def print_name3():
    global j # looks for the global variable
    j = "Lucas" # changes j = "Lee" to j = "Lucas"

print_name3() # calls the function so the global variable sets j = "Lucas"
print(j) # Lucas

### ACTIVITY ###
# 1) Make a variable called "pi" which is set to 0 (we will edit this later)
# 2) After that, make a function called "radius_of_a_circle" which takes 1 argument called "circumference"
# 3) Inside the function, make a variable called "pi" which calls its global counterpart and set it equal to 3.1415
# 4) Finally, this function will return a variable called "radius" which is equal to (circumference)/(2*pi)

pi = 0
def radius_of_a_circle(circumference):
    global pi
    pi = 3.1415
    radius = (circumference)/(2*pi)
    return radius

print(radius_of_a_circle(10)) # 1.5915...
print(radius_of_a_circle(pi)) # 0.5
print(pi) # 3.1415

# Modules #
# When we're writing code, we don't want it all to be in one file as that can get quite lengthy so we can break it up into "modules"
# Modules are different files that hold our code

import module1
module1.one_piece()

# We can also rename our module into something more coherent
import module1 as m1
m1.one_piece()
print(m1.my_games["game1"])
print(m1.computer)
