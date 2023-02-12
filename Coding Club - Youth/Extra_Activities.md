# Extra Activities

## EA 1: Git

### What is Git?

If you're interested in continuing coding as a career, hobby, or anything else, then learning how to use Git is essential. **Git** is what we call a ***version control system***; in other words, its a way to record and save our code similar to how we would save a Google Doc or Powerpoint. Using Git provides an efficient way to save the progress of our code and is a necessary skill for programmers in any industry.

- [Download Git](https://git-scm.com/)
- [Learn Git Branching](https://learngitbranching.js.org/)

### Some Notes

- **Git** and **Github** are NOT the same thing
- **Git**: Version control system tool
- **Github**: Service that uses Git

### Your Goal

Complete every level in the *Main* section's ***Introduction Sequence*** and ***Ramping Up***, and every single level in the *Remote* section from the "Learn Git Branching" website. **Read the instructions of each level carefully because every level teaches something new!**

## EA 2: Vowel Counter

### Description

In this EA, you will make a **Vowel Counter** which checks how many vowels there are in a given string. For this situation, we will count the letters *a*, *e*, *i*, *o*, *u*, and *y* as vowels. Make a function called `vowel_counter()` that takes 1 argument/parameter called `my_statement`. This function will `return` the number of vowels it counted. All of your code should be within `vowel_counter()`. Also, check for cases where someone doesn't input a string (e.g. I input a number into `vowel_counter`) by returning "Please input a string". Here's some starter code for the extra activity:

```python
    def vowel_counter(my_statement):
        # Start your code here
```

To check if you input something that isn't a string, use ``type()``. Check out [Python Type](https://www.geeksforgeeks.org/python-type-function/) for further explanation.

### Examples

Here are some examples of what your function should return:

```python
    print(vowel_counter("among us")) # 3
    print(vowel_counter("City CENTRE commUnity Centre")) # 10
    print(vowel_counter(23423)) # Please input a string
    print(vowel_counter(True)) # Please input a string
    print(vowel_counter('a')) # 1
    print(vowel_counter('A')) # 1
    print(vowel_counter("bc")) # 0
```

## EA 3: Calculator Class

### Description

Make a class/object called **University** which will have the variables of *school_name* (string), *chancellor* (string), *num_of_undergraduates* (number), *num_of_staff* (number), and *is_open* (boolean). This class will also have the ``__init__()`` and ``__str__()`` functions. The ``__str__()`` will return ``[school name] is run by [chancellor] with [num_of_undergraduates] undergraduates and [num_of_staff] staff``. Additionally, make a function called ``calculate_gpa`` in **University** which takes 2 argument called ``grades`` and ``credits`` which are both lists.

### calculate_gpa Explained

Some universities operate on a 4.0 scale whereas others operate on a 4.33 scale. We will be looking at a 4.33 scale which corresponds letter grades to certain numbers. See [SFU's Grading Systems and Policies](http://www.sfu.ca/students/calendar_archive/10.11%20calendar/calendar/for_students/grading.html) chart for what each letter grade means.

Your function of ``calculate_gpa`` should return a number corresponding to someone's GPA between 0 and 4.33. The way GPA is calculated is by adding up each letter grade's corresponding number divided by the number of credits someone receives.

For example, here's a Python representation of calculating GPA:

```python
    grades = ['A+', 'B', 'C-'] # A+ = 4.33, B = 3, C- = 1.67
    credits = [3, 1, 6]
    gpa = (4.33*3) + (3*1) + (1.67*6)
    total_credits = 3 + 1 + 6
    final_gpa = gpa / total_credits
```

### Examples

Here are some examples of what your class should show:

```python
    u1 = University("SFU", "Tamara Vrooman", 25690, 1095, True)
    u2 = University("UBC", "Steven Point", 53872, 6296, True)
    gr1 = ['A', 'B', 'A+', 'C']
    cr1 = [3, 3, 3, 4]
    gr2 = ['F', 'A-', 'A+', 'B+']
    cr2 = [2, 3, 3, 3]
    print(u1) # SFU is run by Tamara Vrooman with 25690 undergraduates and 1095 staff
    print(u2) # UBC is run by Steven Point with 53872 undergraduates and 6296 staff
    print(u1.calculate_gpa(gr1, cr1)) # 3.23
    print(u2.calculate_gpa(gr2, cr2)) # 3.09000...
```
