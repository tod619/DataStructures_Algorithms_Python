# Implementation of a Queue abstract data type
#14/10/2023

# queue is FIFO First In First Out
class Queue:

    def __init__(self):
        self.queue = []

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
    
my_queue = Queue()
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(6)
my_queue.enqueue(8)
my_queue.enqueue(10)
my_queue.enqueue(12)
my_queue.enqueue(14)
my_queue.enqueue(16)
my_queue.enqueue(18)

print(f"The size of my queue is: {my_queue.size_of_queue()}")
print(f"The first item on my queue is: {my_queue.peek()}")

while my_queue.is_empty() != True:
    print(my_queue.dequeue())

print(f"The size of my queue when all the itmes have been dequeued is: {my_queue.size_of_queue()}")