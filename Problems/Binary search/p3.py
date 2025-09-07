from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        # Find the pivot where the rotation happened
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # Pivot is in the right half
                # Example: [4,5,6,7,0,1,2]
                # Here, nums[m]: 5 > nums[r]: 2
                print(f'nums[m]: {nums[m]} > nums[r]: {nums[r]}')
                l = m + 1
            else:
                print(f'nums[m]: {nums[m]} <= nums[r]: {nums[r]}')
                r = m

        pivot = l # or r, since l == r
        
        print(f'Pivot: {pivot}')

        def binary_search(left: int, right: int) -> int:
            print(f'In binary search: left={left}, right={right}')
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)
                
# Input:
nums = [4,0,1,2,3]
target = 2
sol = Solution()
print(sol.search(nums, target))

# Output: 3