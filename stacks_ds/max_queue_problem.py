# Implement the Queue data struct with a stack
# 16/10/2023

# queue is FIFO First In First Out
class Queue:

    def __init__(self):
       # Use 1 stack for enqueueu
       self.enqueue_stack = []
       # Use 1 stack for dequeue
       self.dequeue_stack = []

    # Add an itme to the stack 0(1)
    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty....")
        
        if len(self.enqueue_stack_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

        