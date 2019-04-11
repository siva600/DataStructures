from stack import Stack


def bin(n):
    binary = []
    while n != 0:
        k = n//2
        binary.append(n%2)
        n = k
    return '0b' + ''.join(map(str, binary[::-1]))


# using recursion
def convert_to_binary(n):
    if n > 1:
        convert_to_binary(n // 2)
        print(n % 2)


# using stack
def dec_to_bin(number):
    s = Stack()
    while number > 0:
        remainder = number % 2
        s.push(remainder)
        number = number//2

    binary_number = ""
    while not s.isempty():
        binary_number += str(s.pop())
    return binary_number

