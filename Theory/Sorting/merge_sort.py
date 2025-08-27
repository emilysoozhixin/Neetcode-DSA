from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, \"{self.value}\")"  # for pretty printing

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    
    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[List[Pair]]:
        
        # Base case
        if e - s + 1 <= 1:
            return pairs
        
        mid = (s + e) // 2
        
        self.mergeSortHelper(pairs, s, mid)
        self.mergeSortHelper(pairs, mid + 1, e)

        self.merge(pairs, s, mid, e)

        return pairs
    
    def merge(self, arr: List[Pair], s: int, mid: int, e: int) -> None:

        left = arr[s : mid + 1]
        right = arr[mid + 1 : e + 1]

        i = 0  # Pointer for left
        j = 0  # Pointer for right
        k = s  # Pointer for main array

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
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
pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry"), Pair(1, "date"), Pair(9, "elderberry")]
solution = Solution()
print(solution.mergeSort(pairs)) 

# Output:
# [(1, "date"), (2, "banana"), (5, "apple"), (9, "cherry"), (9, "elderberry")]

