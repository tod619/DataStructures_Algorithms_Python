# a Function to return the max item on the stack
# 15/10/2023

class Stack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):

        if self.stack_size < 1:
            return
        
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def stack_size(self):
        return len(self.stack)
    
    

    

