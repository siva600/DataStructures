# program to check first upper case letter in the string
# iterative method - O(n) complexity


def find_upper_iterative(s):
    for ch in range(len(s)):
        if s[ch].isupper():
            return s[ch]
    return "No case found"


# recursive method - O(1) complexity
def find_upper_recursive(s, index=0):
    if s[index].isupper():
        return s[index]
    if index == len(s) - 1:
        return "No upper case found"
    return find_upper_recursive(s, index + 1)


print(find_upper_iterative("siva Programming"))
print(find_upper_iterative("siva Programming"))

