# A B C D
#
# D
# C
# B
# A
# push, pop, empty stack.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if Stack.isempty(self):
            return 0
        else:
            return self.items.pop()

    def get_stack(self):
        return self.items

    def isempty(self):
        return self.items == []

    def peek(self):
        if not self.isempty():
            return self.items[-1]

