def selection_sort(array):
    for divider_position in range(len(array)):
        smallest = divider_position

        for j in range(divider_position + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j

        (array[divider_position], array[smallest]) = (array[smallest], array[divider_position])

list1 = [5, 2, 4, -6, 1, 3]
list2 = [3, 6, 1, 2, 8]
list3 = [0, 3, 1, 19, 20, 13, 40]

selection_sort(list1)
selection_sort(list2)
selection_sort(list3)

print(list1) # [-6, 1, 2, 3, 4, 5]
print(list2) # [1, 2, 3, 6, 8]
print(list3) # [0, 1, 3, 13, 19, 20, 40]