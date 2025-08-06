class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head 
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data, end=" -> ")
                curr = curr.next
            print("None")

node = Node(1)
ll_1 = LinkedList(node)
ll_1.insert_at_beginning(2)
ll_1.insert_at_beginning(3)
ll_1.insert_at_end(4)
ll_1.print()
