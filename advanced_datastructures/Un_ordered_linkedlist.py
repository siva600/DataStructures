###################################################################################
# node holds atleast 2 piece of info, 1st The node must contain the list
# item itself.
# Each linked list has an entry point - head of the list. All the other nodes
# can be reached by accessing the first node following next links.
# Each time we add a new item, it will be the first item in the list and existing
# items will be linked to this new first item, so that they follow.
# Now adding item can be done in 2 steps. 1) Each item must reside in a new node.
# 2) Always we modify the head, to refer to new node.
# 3) set next reference of the new node to refer to the old first node of the list.
#
# ################################################################################


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        found = False
        current = self.head

        while current != None and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

myNode = Node(93)

print(mylist.search(93))
