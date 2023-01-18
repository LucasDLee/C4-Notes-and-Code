### Class 1 ###

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