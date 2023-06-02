
### Class 7 ###
print("\nClass 7")

# Recursion #
print("\nTopic: Recursion")

# A way to simulate a loop WITHOUT using a loop
# Called recursion because we repeatedly call the same function to do a certain task

## Recursive Functions ##

# Factorial (https://en.wikipedia.org/wiki/Factorial) is a way to start at some number and get the product of all numbers that come before it
# e.g. 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# e.g. 3! = 3 * 2 * 1 = 6
# e.g. 1! = 1
# e.g. (-9)! = error

# Simulate factorial with a loop
print("Factorial")
def factorial_loop(my_num):
    product = 1
    for x in range(1, my_num + 1):
        product *= x
    return product

print(factorial_loop(6)) # 720
print(factorial_loop(1)) # 1
print(factorial_loop(3)) # 6

# Simulate factorial with recursion
def factorial_recursion(my_num):
    if my_num < 1:
        return 1

    return factorial_recursion(my_num - 1) * my_num

print(factorial_recursion(6)) # 720
print(factorial_recursion(1)) # 1
print(factorial_recursion(3)) # 6


# The Fibonacci sequence (https://en.wikipedia.org/wiki/Fibonacci_sequence) gets the sum of the previous 2 numbers to get the next number in the sequence
# Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
print("\nFibonacci")
def fibonacci_loop(x):
    if x <= 0:
        return None  # return None for invalid input
    elif x == 1:
        return 0  # First Fibonacci number is 0
    elif x == 2:
        return 1  # Second Fibonacci number is 1

    prev, curr = 0, 1

    for _ in range(3, x + 1):
        prev, curr = curr, prev + curr # swaps the 2 variables and sets curr as prev + curr

    return curr

print(fibonacci_loop(8)) # 13 (because it is the 8th position in the sequence)
print(fibonacci_loop(3)) # 2 (because it is the 3rd position in the sequence)
print(fibonacci_loop(0)) # None


def fibonacci_recursive(x):
    if x <= 0:
        return None  # return None for invalid input
    elif x == 1:
        return 0  # First Fibonacci number is 0
    elif x == 2:
        return 1  # Second Fibonacci number is 1

    return fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2)


print(fibonacci_recursive(8)) # 13 (because it is the 8th position in the sequence)
print(fibonacci_recursive(3)) # 1 (because it is the 3rd position in the sequence)
print(fibonacci_recursive(0))

### ACTIVITY ###
# 1) Make a function called count_down() that takes 1 argument called start_time. start_time is a number
# 2) Inside of your function, print to the console "T minus " + str(start_time) + " seconds until something happens" and recursively call your function until start_time hits 0'
# 3) When count_down() hits 0, print to the console: "Something happened!"

def count_down(start_time):
    if(start_time < 1):
        print("Something happened!")
        return 0
    print("T minus " + str(start_time) + " seconds until something happens")

    count_down(start_time - 1)

count_down(5)
# T minus 5 seconds until something happens
# T minus 4 seconds until something happens
# T minus 3 seconds until something happens
# T minus 2 seconds until something happens
# T minus 1 seconds until something happens
# Something happened!



### Class 8 ###
print("\nClass 8")

# UBC Grades
# https://ubcgrades.com/api-reference

# New Topic: Pandas, Numpy, Matplotlib, and CSV Files #
# CSV files are similar to JSON; they are another way to store data
print("\nTopic: Data Manipulation")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Get the UBC data from its CSV file
ubc_data = pd.read_csv("ubc-grades.csv")

# Set the data into a DataFrame (type of data organization)
ubc_data = pd.DataFrame(ubc_data)
print(ubc_data)

# Using Matplotlib, we can put all of this data into a graph

# What this shows us is the average final grade per course name. However, its super condensed so we may want to combine the data
plt.plot(ubc_data["course_title"], ubc_data["average"], 'b.')
plt.legend(["Average Final Grade"]) # labels the blue dots
plt.xlabel("Course Name")
plt.xticks(rotation=90) # rotates the x-axis labels to 90 degrees
plt.ylabel("Average Grade")
plt.show()

# Here, we can combine all of our departments and get the average grade for each of them
group_by_department = ubc_data.groupby(["subject"])
get_department_average = group_by_department.aggregate({'average': 'mean'}).reset_index()
print(get_department_average)

plt.plot(get_department_average["subject"], get_department_average["average"], 'b.')
plt.legend(["Average Final Grade"]) # labels the blue dots
plt.xlabel("Course Name")
plt.xticks(fontsize=5, rotation=45) # rotates the x-axis labels to 90 degrees w/ a fontsize of 5px
plt.ylabel("Average Grade")
plt.figure(figsize=(100, 6)) # set graph size
plt.show()

# However, that's hard to read. Instead, we can just get the grades of a certain department
get_comp_sci = ubc_data[ubc_data["subject"] == "CPSC"] # get all comp sci subjects
print(get_comp_sci)

# Extract x and y values from the DataFrame
x = get_comp_sci["course"] # course number
y = get_comp_sci["average"] # average grade

# # Plot the data points
plt.plot(x, y, 'b.')

# Find the best fit line
m, b = np.polyfit(x, y, 1)

# Plot the best-fit line
plt.plot(x, m*x + b, 'r-') # slope: y = mx + b

plt.xlabel("CPSC Course Number")
plt.ylabel("Grade")
plt.show()

### ACTIVITY ###
# Using the UBC Data, your goal is to make a graph that shows the average grade each course taught by a certain professor
# 1) Look and filter for the educator called "Gabrielle Lam". You should see 17 rows
# 2) If you print out your filtered results, you'll see "Engineering Materials Laboratory" and "Engineering Materials" are offered multiple times. For this part, let us group by the "course_title" and calculate the average grade to get the "mean"
#   2.1) You should get 4 rows as a result
# 3) Once you've done that, plot your result on the graph with the course_title as the x-axis and average as the y-axis

get_educator = ubc_data[ubc_data["educators"] == "Gabrielle Lam"] # should see 17 rows
print(get_educator)
combine_grades = get_educator.groupby(["course_title"])
get_average = combine_grades.aggregate({'average': 'mean'}).reset_index()
print(get_average)
plt.plot(get_average["course_title"], get_average["average"], 'b.')
plt.xticks(rotation=45)
plt.show()