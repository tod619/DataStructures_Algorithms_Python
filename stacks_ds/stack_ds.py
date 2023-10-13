# Stack implementation
# Stack is LIFO (Last In First Out)
# 13/10/2023

class Stack:

    def __init__(self):
        self.stack = []

    # Create push method that inserts items onto the stack Big O(1)
    def push(self, data):
        self.stack.append(data)

    # Create pop method that returns the item at the top of the stack the Last In Big O(1)
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data 
