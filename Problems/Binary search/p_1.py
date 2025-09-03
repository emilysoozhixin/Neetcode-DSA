from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m = num of rows
        # n = num of col 

        l_m = 0
        r_m = len(matrix) - 1
        l_n = 0
        r_n = len(matrix[0]) - 1

        while l_m <= r_m:
            mid = (l_m + r_m) // 2

            if target > matrix[mid][0]:
                print(mid)
                l_m = mid + 1

            elif target < matrix[mid][0]:
                print(mid)
                r_m = mid - 1
            
            else:
                return True
            
        row = r_m
        if row < 0 or row >= len(matrix):
            return False
        while l_n <= r_n:
            mid = (l_n + r_n) // 2

            if target > matrix[row][mid]:
                l_n = mid + 1

            elif target < matrix[row][mid]:
                r_n = mid - 1
            
            else:
                return True 

        return False

# Input: 
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15
sol = Solution()
print(sol.searchMatrix(matrix, target))

# Output: False