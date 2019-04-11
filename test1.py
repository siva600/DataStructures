class Node:
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def contents(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)

    def reverse_iterative(self):
        prev = None
        current = self.head
        while current is not None:
            current.next = prev

    def get(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def delete(self, index):
        if index >= self.length():
            print("index out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            tmp = current_node
            current_node = current_node.next
            if current_index == index:
                tmp.next = current_node.next
                return
            current_index += 1


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

length = my_list.length()
my_list.contents()
print(length)

my_list.delete(3)
print(my_list.contents())
