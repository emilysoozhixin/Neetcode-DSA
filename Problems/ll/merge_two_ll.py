from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals) if vals else "None"

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    print("Starting merge...")
    print("List1 head:", list1.val if list1 else None)
    print(f"List1:", end="")
    print_linked_list(list1)
    print("List2 head:", list2.val if list2 else None)
    print(list2)

    if list1 is None:
        return list2

    if list2 is None:
        return list1
    
    newList = None

    if list1.val < list2.val:
        newList = list1
        list1 = list1.next
        print(f"Initial newList from List1: {newList}")
    else:
        newList = list2
        list2 = list2.next
        print(f"Initial newList from List2: {newList}")

    curr = newList

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return newList

# Helpers
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# Example usage
list1 = build_linked_list([1,2,4])
list2 = build_linked_list([1,3,5])

merged = mergeTwoLists(list1, list2)
print("Merged result:")
print_linked_list(merged)