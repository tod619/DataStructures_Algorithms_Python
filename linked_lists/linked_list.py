# Linked List Implementation
# 10/10/2023

from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
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
    
    # Remove item from the list 0(N) Linear runtime
    def remove_item(self, data):
        
        # if the linked list is empty return
        if self.head is None:
            return
        
        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # If the data is not in the Linked list
        if actual_node is None:
            return
        
        # Update the references
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node
            



    # vist every node in the list 0(N)
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start(15)
    linked_list.insert_start(25)
    linked_list.insert_end(100)
    linked_list.insert_end(700)

    linked_list.traverse()

    linked_list.remove_item(10)

    print("\n********************\n")

    linked_list.traverse()