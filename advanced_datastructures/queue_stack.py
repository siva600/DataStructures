class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False

    def pop(self):
        if len(self.stack) <= 0:
            return "Empty Stack"
        return self.stack.pop()

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def pop(self):
        if len(self.queue) <= 0:
            return "Empty Queue"
        return self.queue.pop()

    def size(self):
        return len(self.queue)


class Deque:  # Deque implementation based on python list
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # O(N)                              # Equivalent Python deque methods
    def addFront(self, item):  # appendLeft
        self.items.insert(0, item)

    # O(1)
    def addRear(self, item):  # append
        self.items.append(item)

    # O(N)
    def removeFront(self):  # popLeft
        return self.items.pop(0)

    # O(1)
    def removeRear(self):  # pop
        return self.items.pop()

    def size(self):
        return len(self.items)
