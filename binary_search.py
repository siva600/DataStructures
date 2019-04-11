import sys
# sys.setrecursionlimit(1000)


def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 42))


def binary_search(list, item):
    low = 0
    high = len(list) -1
    while low <=high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None




