# linear search


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Iterative binary search


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high)//2
        if target == data[middle]:
            return True
        elif target < data[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return False

# recursive_binary_search


def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        middle = (low + high)//2
        if target == data[middle]:
            return True
        elif target < data[middle]:
            return binary_search_recursive(data, target, low, middle - 1)
        else:
            return binary_search_recursive(data, target, middle + 1, high)


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 28
print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))
