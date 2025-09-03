import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l

# Input: 
piles = [1,4,3,2]
total = sum(piles)
print(total)
h = 9

sol = Solution()
print(sol.minEatingSpeed(piles, h))
# Output: 2