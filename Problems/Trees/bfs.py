from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        q = deque()

        if root:
            q.append(root)
        
        while q:
            for i in range (len(q)):
                curr = q.popleft()
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
                if i == len(q)-1:
                    res.append(curr.val)
        print(f'res: {res}')
        return res
    
# Input: 
sol = Solution()
root=TreeNode(1)
root.left=TreeNode(2)
print(sol.rightSideView(root))

# Output: [1,2,5]