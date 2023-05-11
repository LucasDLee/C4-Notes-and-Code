### Class 1 ###
print("\nClass 1\n")

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

class MyCity:
    def __init__(self, c, p, g, hc):
        self.city_name = c
        self.population = p
        self.gdp = g
        self.has_costco = hc

    def __str__(self):
        return (self.city_name + " has " + str(self.population) + " people with a GDP of " + str(self.gdp) + ". Also, Costco is " + str(self.has_costco))

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


store1 = MyStore("Vulcan", 1, 6, True, "Walmart", 1900, False)
print(store1)
print(store1.check_if_open())



### Class 2 ###
print("\nClass 2\n")

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
#   1.1) If everything is all good, return the difference of x and y
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
print("\nModules")
# When we're writing code, we don't want it all to be in one file as that can get quite lengthy so we can break it up into "modules"
# Modules are different files that hold our code

import module1
module1.one_piece()

# We can also rename our module into something more coherent
import module1 as m1
m1.one_piece()
print(m1.my_games["game1"])
print(m1.computer)




### Class 3 ###
print("\nClass 3\n")

# Regular Expressions (RegEx) #
print("\nRegEx")
# When we want a user to input a specific set of words or numbers, we want to account for all scenarios and we can use RegEx to create a specific string format for that.

# RegEx Checker: https://regex101.com/
# RegEx Flags: https://pynative.com/python-regex-flags/
# RegEx Library: https://docs.python.org/3/library/re.html
# RegEx Syntax (pattern formatting): https://docs.python.org/3/library/re.html#regular-expression-syntax

import re # import RegEx
name = "Lucas"

# []: Set of characters/numbers
all_lowercase_letters = re.findall("[a-z]", name)
# findall(your RegEx pattern, your string, flags=0): Finds all instances of your string's pattern
print(all_lowercase_letters) # returns a LIST

sin = "123456789"
all_numbers = re.findall("[0-9]", sin)
print(all_numbers)

# {}: Exactly that number of occurences
my_pattern = re.compile(r"\w{3}") # builds a RegEx pattern that looks for words with 3 exactly letters
# compile(your RegEx pattern, flags=0) # Builds your RegEx pattern
print(my_pattern.findall("Abe has a long sword and short bow"))

single_letter_search = re.search("a", name) # can also do "[a]"
# search(RegEx pattern you're looking for, your string, flags=0): Returns the first item it finds
print(single_letter_search)

lowercase_search = re.search("[a-z]", name)
print(lowercase_search) # matches with 'u' which is the 1st lowercase letter
uppercase_search = re.search("[A-Z]", name) # matches with 'L' which is the 1st uppercase letter
print(uppercase_search)

name = "Lucas Lee"
search_everything = re.search("[a-zA-z]+", name)
print(search_everything)

# *: Zero or more occurences
# +: One or more occurences
c4 = "City Centre Community Centre"
zero_search = re.search("[a-z]*", c4)
print(zero_search)
one_search = re.search("[a-z]+", c4)
print(one_search)

debit_card = "1234567890123456" # 16 digits
print(re.findall("[0-9]", debit_card)) # prints each individual number
print(re.findall("[0-9]{16}", debit_card)) # prints the entire debit card together

### ACTIVITY ###
# 1) Make a function called valid_email(). This function takes 1 argument of user_email
# 2) All emails follow a certain format. Some combination of letters & numbers followed by the @ symbol. After that is the domain name (name of the website) with letters and numbers followed by the websites's top- level domain (.net, .com, .org, .ca, etc.) which consists of letters only:
# - For example, c4@gmail1.com is valid
# - For example, c4@gmail2.123com is not valid (because the domain name has numbers in it)
# 3) Using RegEx, check if user_email is valid by returning a boolean following the format in #2

# Some notes:
# - I would recommend you use findall()
# - You might get an IndexError so use exception handling to overcome that. Return false for that error

def valid_email(user_email):
    try:
        is_valid = re.findall("[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-zA-Z]+", user_email)
        return is_valid[0] == user_email    
    except IndexError:
        return False

print(valid_email("32423@a.o")) # True
print(valid_email("32423@a.")) # False
print(valid_email("c4@gmail1.com")) # True
print(valid_email("abc@")) # False
print(valid_email("c4@gmail2.123com")) # False
print(valid_email("c4@3243.com")) # True
print(valid_email("a@a.a")) # True
print(valid_email(".com")) # False



### Class 4 ###
print("\nClass 4\n")

# JavaScript Object Notation (JSON) #

# A style of syntax for storing and exchanging data
# You don't need to know JavaScript to use JSON

import json

person = '{ "name": "Lucas", "age": 21, "is_employed": true }'

# Similar to a Python Dictionary
# person = {
#     "name": "Lucas",
#     "age": 21,
#     "is_employed": True
# }

load_json = json.loads(person) # converts person into a Python Dictionary
print(load_json)

# Opening JSON file
open_my_account = open("json-explanation.json")
my_account = json.load(open_my_account)
print(my_account)
print(my_account["name"])

# Application Programming Interfaces (APIs) #
# A way for different softwares to connect with each other and send data
# Many APIs use JSON to send data

# https://api.nasa.gov/

# Nasa's Astronomy Picture of the Day (APOD)
import requests  # used for getting API requests
import json

response_API = requests.get('https://api.nasa.gov/planetary/apod?api_key=dJsaDmJOddJO9frfefQ4JagcAJSeXhuJGbe6SliB') # call the API
data = response_API.text  # change the API request into plain text
parse_json = json.loads(data)  # load the API into JSON
print(parse_json)
print(parse_json["explanation"])
print(parse_json["url"])

### ACTIVITY ###
# Display any image to your GUI using NASA's Mars Rover Photos API
# 1) Using the links provided to us (https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY), first identify which part of this JSON file would give us the image
# 2) Once you've identified where the image link is, print it to the console by doing the following:
#   - Call the API using request
#   - Change your request into plain text
#   - Load your API into JSON format
#   - Print it out. To get your image, you should follow this format: ['photos'][0][what would you put here to get your image?]

# Set up API => JSON data conversion
get_mars_api = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY") # get API
mars_data = get_mars_api.text # sets JSON to plain text
load_mars_api = json.loads(mars_data) # API => JSON
print(load_mars_api['photos'][0]['img_src'])
# img_data = requests.get(load_mars_api['photos'][0][what would you put here to get your image?]).content




### Class 5 ### 
print("\nClass 5\n")

# Calling NASA's APOD API
response_API = requests.get('https://api.nasa.gov/planetary/apod?api_key=dJsaDmJOddJO9frfefQ4JagcAJSeXhuJGbe6SliB') # call the API
data = response_API.text  # change the API request into plain text
apod_json = json.loads(data)  # load the API into JSON

# Graphical User Interfaces #
import tkinter as tk
from PIL import Image, ImageTk
import io

window = tk.Tk()
window.title(apod_json["title"])  # set a title to your GUI
window.geometry("500x450")  # set your GUI size (width x height)

# Download the image to your workplace
response = requests.get(apod_json["url"])
img_data = response.content

# Open your image from the data
load_img = Image.open(io.BytesIO(img_data))

# Add your uploaded image to Tkinter
gui_image = ImageTk.PhotoImage(load_img)

# Create a label with the image to put it into your GUI
add_image = tk.Label(window, image=gui_image)
add_image.pack()

# Create a label with some descriptive text
add_description = tk.Label(window, text=apod_json["explanation"])
add_description.pack()

window.mainloop()  # display everything in your GUI


### ACTIVITY ###
# Using the code you wrote for the previous activity, display your Mars Rover image to your GUI

# Set up GUI
window = tk.Tk()
window.geometry("500x450")  # set your GUI size (width x height)

# Mars Rover Image Code
get_mars_api = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY") # get API
mars_data = get_mars_api.text # sets JSON to plain text
load_mars_api = json.loads(mars_data) # API => JSON

response = requests.get(load_mars_api["photos"][0]["img_src"])
img_data = response.content

# Create a Tkinter window
root = tk.Tk()

# Open the image from the image data
img = Image.open(io.BytesIO(img_data))

# Convert the image to a Tkinter PhotoImage
photo = ImageTk.PhotoImage(img)

# Create a label with the image
label = tk.Label(root, image=photo)
label.pack()

# Run the Tkinter event loop
root.mainloop()