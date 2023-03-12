# Sorting Algorithms

## Description

In this final activity, you will be looking at something called "Sorting Algorithms" which orders items from smallest to largest.

## Selection Sort

Selection sort is a type of sorting algorithm that divides a list (e.g. ``[6 7 1 2 0]``) into 2 parts: a **sorted** side on the left and an **unsorted** side on the right.

Here is a gif to demonstrate that:

![selection sort gif](selectionSort.gif)

**Gif Explanation**:

1) First, it goes through the list until it finds the smallest value (in this case, #1). Then, it **swaps** the smallest value to the **left of the line** with whichever number is on the **right of the line**.
2) It moves to the right 1 time and checks the list again until it finds the smallest value. Once it does that, it swaps the two values mentioned above.
3) This will continue until your algorithm gets to the end of the list.

Your goal is to recreate this algorithm in Python. Here's some test cases to help you with that:

```python
    list1 = [5, 2, 4, -6, 1, 3]
    list2 = [3, 6, 1, 2, 8]
    list3 = [0, 3, 1, 19, 20, 13, 40]

    selection_sort(list1)
    selection_sort(list2)
    selection_sort(list3)

    print(list1) # [-6, 1, 2, 3, 4, 5]
    print(list2) # [1, 2, 3, 6, 8]
    print(list3) # [0, 1, 3, 13, 19, 20, 40]
```

## Bubble Sort

Bubble sort is a type of sorting algorithm that compares two adjacent numbers (or two numbers next to each other) and swaps them if the bigger number is on the left.

Here is a gif to demonstrate that:

![bubble sort gif](bubbleSort.gif)

**Gif Explanation**:

1) The *red rectangle* looks at 2 numbers. If the larger number is on the left, it swaps the two
2) Then, it continues to the next 2 numbers. It checks if the larger number is on the left. If so, it swaps. Otherwise, it moves on
3) Once the *red rectangle* gets to the end, it returns to the beginning of the list to do the same thing in steps #1 and #2
4) This will repeat until the list is sorted

Your goal is to recreate this algorithm in Python. Here's some test cases to help you with that:

```python
    list1 = [5, 2, 4, -6, 1, 3]
    list2 = [3, 6, 1, 2, 8]
    list3 = [0, 3, 1, 19, 20, 13, 40]

    bubble_sort(list1)
    bubble_sort(list2)
    bubble_sort(list3)

    print(list1) # [-6, 1, 2, 3, 4, 5]
    print(list2) # [1, 2, 3, 6, 8]
    print(list3) # [0, 1, 3, 13, 19, 20, 40]
```
