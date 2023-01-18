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

In this EA, you will make a **Vowel Counter** which checks how many vowels there are in a given string. For this situation, we will count the letters *a*, *e*, *i*, *o*, *u*, and *y* as vowels. Make a function called `vowel_counter()` that takes 1 argument/parameter called `my_statement`. This function will `return` the number of vowels it counted. All of your code should be within `vowel_counter()`. Also, check for cases where someone doesn't input a string (e.g. I input a number into `vowel_counter`). Here's some starter code for the extra activity:

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
