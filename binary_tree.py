class BinaryTree(object):
    """docstring for BinaryTree"""
    # Building the root.
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    # accessor elements
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.right = Node(4)
# tree.root.left = Node(5)

r = BinaryTree('a')

print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild()) # prints an object.
print(r.getLeftChild().getRootVal())

r.insertRight('C')
print(r.getRightChild())
print(r.getRightChild().getRootVal())

r.getRightChild().setRootVal('Hello')
print(r.getRightChild().getRootVal())
