from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f"({self.key}, \"{self.value}\")"

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        return self.quickSortHelper(pairs, 0, n - 1)

    def quickSortHelper(self, pairs: List[Pair], s: int, e: int, depth: int = 0) -> List[Pair]:
        indent = "  " * depth
        if e - s + 1 <= 1:
            print(f"{indent}Base case: {pairs[s:e+1]}")
            return pairs

        print(f"{indent}QuickSort called on {pairs[s:e+1]}; s={s}, e={e}")

        pivot = pairs[e]
        left = s # pointer for left side
        print(f"{indent}Chosen pivot: {pivot}")
        for i in range(s, e):
            print(f"{indent}Considering {pairs[i]} at index {i}")
            if pairs[i].key < pivot.key:
                print(f"{indent}Swapping {pairs[i]} and {pairs[left]}")
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1
                print(f"{indent}Array after swap: {pairs}")
            print(f"{indent}Left pointer at index {left}, value {pairs[left] if left < len(pairs) else 'N/A'}")

        # Place pivot in correct position
        print(f"{indent}Placing pairs[e={e}] at index {left}")
        pairs[e] = pairs[left]
        print(f"{indent}Array before placing pivot: {pairs}")
        print(f"{indent}Swapping pivot {pivot} with {pairs[left]}")
        pairs[left] = pivot
        print(f"{indent}Array after placing pivot: {pairs}")
        self.quickSortHelper(pairs, s, left - 1, depth + 1)
        self.quickSortHelper(pairs, left + 1, e, depth + 1)

        return pairs

# Input:
# pairs = [Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")]
pairs = [Pair(1, "x"), Pair(2, "y"), Pair(3, "z"), Pair(2, "a"), Pair(1, "b"), Pair(3, "c")]
sol = Solution()
print(sol.quickSort(pairs))

# Output:
# [(2, "dog"), (3, "bird"), (3, "cat")]
# [(1, "b"), (1, "x"), (2, "y"), (2, "a"), (3, "c"), (3, "z")]