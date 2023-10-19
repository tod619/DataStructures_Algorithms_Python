# An Implementation of a binary search tree
# 17/10/2023

class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchtree:

    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # Go to left sub tree
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)

        else:
            # Go to the right sub tree
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    def get_min(self):
        if self.node:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node:
            self.get_min_value(node.left_node)

        return node.data
    
    def get_max(self):
        if self.node:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            self.get_min_value(node.right_node)

        return node.data
        
        