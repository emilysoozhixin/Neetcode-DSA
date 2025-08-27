class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail 
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next 
        while curr and index > 0:
            curr = curr.next 
            index -= 1
        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode, next, prev = ListNode(val), self.head.next, self.head
        prev.next = newNode
        next.prev = newNode
        newNode.next = next 
        newNode.prev = prev 

    def addAtTail(self, val: int) -> None:
        newNode, next, prev = ListNode(val), self.tail, self.tail.prev
        prev.next = newNode
        next.prev = newNode
        newNode.next = next 
        newNode.prev = prev 

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            newNode, next, prev = ListNode(val), curr, curr.prev
            prev.next = newNode
            next.prev = newNode
            newNode.next = next 
            newNode.prev = prev 

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            next, prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

