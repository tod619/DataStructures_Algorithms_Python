# Linked List Implementation
# 10/10/2023

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0
    
    # Add a node at the start of the list 0(1) constant time
    def insert_start(self, data):
        self.num_of_nodes += 1

        new_node = Node(data)

        # Check if the first node is empty if it is the new node is the head
        if self.head is None:
            self.head = new_node
        else:
            # This is executed when the Linked List is not empty we update the references
            new_node.next_node = self.head
            self.head = new_node

    # Insert at the end of the list
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            # This is why the runtie is 0(N) linear run time
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node

        

    # Return the size of the list 0(1) constant time
    def size_of_list(self):
        return self.num_of_nodes  