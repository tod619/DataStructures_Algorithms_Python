# An Implementation of a binary search tree
# 17/10/2023

class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent