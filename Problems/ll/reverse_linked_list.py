class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
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

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_two_lists(self, other):
        if not self.head:
            return other
        if not other.head:
            return self
        
        merged_head = None
        if self.head.data < other.head.data:
            merged_head = self.head
            self.head = self.head.next
        else:
            merged_head = other.head
            other.head = other.head.next
        
        current = merged_head
        
        while self.head and other.head:
            if self.head.data < other.head.data:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other.head
                other.head = other.head.next
            current = current.next
        
        if self.head:
            current.next = self.head
        elif other.head:
            current.next = other.head
        
        return merged_head  
    
head = Node(1)
ll = LinkedList(head)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.print()
'''Test reverse method'''
# ll.reverse()
# ll.print()

'''Test merge_two_lists method'''
list1 = [1,2,4]
list2 = [1,3,5]

ll1 = LinkedList()
for item in list1:
    ll1.insert_at_end(item)

ll2 = LinkedList()
for item in list2:
    ll2.insert_at_end(item)

merged_head = ll1.merge_two_lists(ll2)
merged_list = LinkedList(merged_head)
merged_list.print()

list3 = []
for item in list3:
    merged_list.insert_at_end(item)
