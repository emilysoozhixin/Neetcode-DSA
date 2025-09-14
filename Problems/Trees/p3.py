from typing import Optional 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        print(f'At node: {root.val}, targetSum: {targetSum}')
        
        res = 0
        res += root.val

        print(f'Current sum: {res}')

        # leaf
        if not root.left and not root.right:
            print(f'Leaf node reached with sum: {res}')
            if root.val == targetSum:
                return True
    
        
        print(f'Going left from node {root.val}')
        if self.hasPathSum(root.left, targetSum - res):
            return True
        print(f'Going right from node {root.val}')
        if self.hasPathSum(root.right, targetSum - res):
            return True
        
        return False

# Input: 
root = TreeNode(-2)
root.right = TreeNode(-3)
targetSum = -5
sol = Solution()
print(sol.hasPathSum(root, targetSum))
# Output: true