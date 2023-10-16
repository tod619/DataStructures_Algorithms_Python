# Get the max value from a queue
# 16/10/2023

# queue is FIFO First In First Out
class Queue:

    def __init__(self):
        self.queue = []
        self.max_queue = []

    def is_empty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def size_of_queue(self):
        return len(self.queue)