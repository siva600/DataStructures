class Node:
    """docstring for Node"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class NodeTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
