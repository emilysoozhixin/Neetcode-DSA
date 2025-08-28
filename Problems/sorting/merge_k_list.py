from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val}->{self.next}"

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for list in lists:
            curr = list
            while curr:
                arr.append(curr.val)
                curr = curr.next
        
        print(f"Arr = {arr}")

        res = self.mergeKListsHelper(arr, 0, len(arr) - 1)

        # Convert arr into [ListNode]
        print(f"Res = {res}")
        tail = ListNode(0)
        head = tail
        for num in range(len(res)):
            tail.next = ListNode(res[num])
            tail = tail.next

        return head.next

    def mergeKListsHelper(self, lists: List[Optional[ListNode]], s: int, e: int) -> Optional[ListNode]:
        
        if e - s + 1 <= 1:  # only one element
            return lists

        mid = (s + e) // 2
        self.mergeKListsHelper(lists, s, mid)
        self.mergeKListsHelper(lists, mid + 1, e)

        self.merge(lists, s, mid, e)

        return lists

    def merge(self, arr: List[Optional[ListNode]], s: int, mid: int, e: int) -> None:        

        left = arr[s : mid + 1]
        right = arr[mid + 1 : e + 1]

        i = 0 
        j = 0 
        k = s

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy any remaining elements from left or right
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    


# Input: 
# lists = [ListNode(1)]
# lists = [[1,2,4],[1,3,5],[3,6]]
lists = [ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(5))), ListNode(3, ListNode(6))]
solution = Solution()
print(solution.mergeKLists(lists))

# Output: [1,1,2,3,3,4,5,6]