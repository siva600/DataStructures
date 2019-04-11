# return sum of items in the list using recursion
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


# find the max item using recursion without slicing.
def max_number(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m = max_number(arr[1:])
        return m if m > arr[0] else arr[0]


# find max item from the list recursively.
def find_max_recursive(s, n):
    if n == 1:
        return s[n - 1]

    else:
        previous = find_max_recursive(s, n - 1)
        current = s[n - 1]
        if previous > current:
            return previous
        else:
            return current
