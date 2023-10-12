# Find the middle node of a linked list
# 12/10/2023




class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):
        # your implementation goes here !!!
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer


    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node
   
         
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


linkked_list = LinkedList()
linkked_list.insert(10)
linkked_list.insert(50)
linkked_list.insert(100)
linkked_list.insert(160)
linkked_list.insert(210)
linkked_list.insert(270)

print(linkked_list.get_middle_node().data)