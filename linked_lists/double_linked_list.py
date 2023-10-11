# Double Linked List Implementation
# 11/10/2023

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert function inserts at the end of the LL allowing for 0(1) inserts
    def insert(self, data):
        new_node = Node(data)

        # When the list is emapty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # when there is at least 1 item in the list
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # A Double Linked List can be traversed both forward and backwards
    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next

    def traverse_reverse(self):
        actual_node = self.tail

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.previous

if __name__ == "__main__":
    my_doulde_linked_list = DoubleLinkedList()

    my_doulde_linked_list.insert(10)
    my_doulde_linked_list.insert(15)
    my_doulde_linked_list.insert(20)
    my_doulde_linked_list.insert(25)
    my_doulde_linked_list.insert(30)

    print("Traverse Forward Through The List\n")
    my_doulde_linked_list.traverse_forward()
    print("\n************************\n")
    print("Traverse The Linked List In Reverse")
    my_doulde_linked_list.traverse_reverse()

