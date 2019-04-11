from stack import Stack


def reverse_string(s):
    stack = Stack()
    for i in range(len(s)):
        stack.push(s[i])
    final_string = ""
    while not stack.isempty():
        final_string += stack.pop()
    return final_string


print(reverse_string("hello there !"))


# string reverse using generator
def string_reverse_generator(x):
    for i in range(len(x)-1, -1, -1):
        yield x[i]


for char in string_reverse_generator("hello there!"):
    print(char)

