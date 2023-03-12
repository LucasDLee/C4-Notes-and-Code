def bubble_sort(array):
    size = len(array)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(size-1):
        # range(size) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, size-i-1):

            # traverse the array from 0 to size-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return 

list1 = [5, 2, 4, -6, 1, 3]
list2 = [3, 6, 1, 2, 8]
list3 = [0, 3, 1, 19, 20, 13, 40]

bubble_sort(list1)
bubble_sort(list2)
bubble_sort(list3)

print(list1) # [-6, 1, 2, 3, 4, 5]
print(list2) # [1, 2, 3, 6, 8]
print(list3) # [0, 1, 3, 13, 19, 20, 40]