
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 1:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

s = Solution()
result = s.climbStairs(3)
print("Result:", result)