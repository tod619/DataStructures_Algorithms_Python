# Double Linked List Implementation
# 11/10/2023

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)