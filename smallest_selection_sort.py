# find smallest number using sorting selection sort
import random


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# selection sort using the above function to find the order
# into a new list.
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


lst = [random.randint(1, 10000) for k in range(10000)]
print(selectionSort(lst))
