from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ''' Recursive approach '''
        res = []
        subset = []

        def dfs(i):
            print(f'At index: {i}')
            if i >= len(nums):
                # Make a deep copy of the current subset

                res.append(subset.copy()) 
                print(f'Added subset to results, res now: {res}')
                return 
            
            # Decision to include nums[i]
            subset.append(nums[i])
            print(f'Include nums[{i}] = {nums[i]}, subset now: {subset}')
            dfs(i + 1)

            # Decision NOT to include nums[i]
            subset.pop()
            print(f'Exclude nums[{i}] = {nums[i]}, subset now: {subset}')
            dfs(i + 1)

        print(f'Starting DFS, nums = [{nums}]')
        dfs(0)
        return res

        # ''' Iterative approach '''
        # res = [[]]
        # for num in nums:
        #     new_subsets = []
        #     for subset in res:
        #         new_subset = subset + [num]   # extend the subset with current number
        #         new_subsets.append(new_subset)
        #     res.extend(new_subsets)           # add all new subsets at once
        # return res



# Input:
nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]