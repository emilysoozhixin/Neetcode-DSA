from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        
        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(combo.copy())
                return
            
            if curr_sum > target:
                print(f'Current sum {curr_sum} exceeds target {target}, backtracking...')
                return
            
            for i in range(start, len(nums)):
                print(f'At index: {i}, current combination: {combo}, current sum: {curr_sum}')
                combo.append(nums[i])
                print(f'backtrack({i}, {curr_sum} + {nums[i]})')
                backtrack(i, curr_sum + nums[i])
                print(f'Backtracking from index: {i}, removing {nums[i]} from combination')
                combo.pop()
        
        backtrack(0, 0)
        return res

# Input:
nums = [2,5,6,9]
target = 9
sol = Solution()
print(sol.combinationSum(nums, target))

# Output: [[2,2,5],[9]]