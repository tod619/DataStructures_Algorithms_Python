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

        if self.stack_size < 1:
            return

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # Create peek function that returns the last item but without removing it Big O(1)
    def peek(self):
        return self.stack[-1] 
    
    # Create is empty function that returns true/false if the stack has an item or not
    def is_empty(self):
        return self.stack == []
    
    # stack_size returns the size of the Stack
    def stack_size(self):
        return len(self.stack)


my_stack = Stack()
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)
my_stack.push(20)
my_stack.push(25)
my_stack.push(30)
my_stack.push(55)

print(f"The last item pushed onto the stack and the first one to pop off is {my_stack.peek()}")

print(f"The size of my stack is: {my_stack.stack_size()}")
while my_stack.is_empty() != True:
    print(my_stack.pop())

print(f"The size of my stack when all the items have been popped off: {my_stack.stack_size()}")
