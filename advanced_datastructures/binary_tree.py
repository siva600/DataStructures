# build binary tree, traverse the tree, search the tree, delete a node,
# find root node, find height of tree
# transform list to tree


from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)

print(root)
