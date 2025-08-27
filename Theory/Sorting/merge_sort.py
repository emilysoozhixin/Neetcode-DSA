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
        
        states = []

        for i in range(len(pairs)):
            j = i - 1
            while j >= 0 and pairs[i].key < pairs[j].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -= 1

            states.append(pairs[:])
            print(f"After pass {i}: {pairs}") 

        return states

# Input:
pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]
solution = Solution()
print(solution.insertionSort(pairs)) 

# Output:
# [[(5, "apple"), (2, "banana"), (9, "cherry")], 
#  [(2, "banana"), (5, "apple"), (9, "cherry")], 
#  [(2, "banana"), (5, "apple"), (9, "cherry")]]

