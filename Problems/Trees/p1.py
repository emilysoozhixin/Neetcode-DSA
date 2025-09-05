from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if val > root.val:
            print("going right")
            return self.searchBST(root.right, val)
        elif val < root.val:
            print("going left")
            return self.searchBST(root.left, val)
        else:
            # val == root.val, print subtree
            return root
        
# Input: 
# root = [4,2,7,1,3]

# You need something like
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

val = 2
sol = Solution()
print(sol.searchBST(root, val))

