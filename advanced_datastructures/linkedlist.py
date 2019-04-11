# https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
from node import Node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # O(1) complexity
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # O(n) Complexity
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # O(n) complexity
    def search(self, data):
        current = self.head
        found = False
        while current:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    # O(n) complexity
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data doesn't exist")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def reverse_iterative(self):
        # head-> 4->2->3 -> None
        # None <-4<-2-<-3 <- Head
        previous = None
        current = self.head
        while current:
            temp = current.next_node # storing the next value in a temporary variable.
            current.next_node = previous
            previous = current
            current = temp
        self.head = previous




