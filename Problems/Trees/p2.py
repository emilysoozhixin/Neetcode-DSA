from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

# 1. get root (0th index of pre)
# 2. get left subt by taking lhs of root
# 3. get right subt by taking rhs of root


class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int], depth=0) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)

        # pre = [1,2,3,4]
        # in = [2,1,3,4]
        # left
        # pre[1:mid+1], in[:mid]
        # right
        # pre[mid+1:], in[mid+1:]

        # Debug with indentation for readability
        indent = "  " * depth
        print(f"{indent}Building node {root_val}")
        print(f"{indent}  preorder: {preorder}")
        print(f"{indent}  inorder : {inorder}")
        print(f"{indent}  mid index: inorder[{mid}]")
        print(f"{indent}  left inorder : {inorder[:mid]}")
        print(f"{indent}  right inorder: {inorder[mid+1:]}")

        # Recurse with depth+1 to indent further
        print(f"{indent}Recursing to build left subtree of {root_val}")
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid], depth+1)
        print(f"{indent}Recursing to build right subtree of {root_val}")
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:], depth+1)

        return root
    
    def printTree(self, root):
        if not root:
            print([])
            return
        
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)

        # trim trailing None values
        while res and res[-1] is None:
            res.pop()

        print(res)

# Input:
preorder = [1,2,3,4]
inorder = [2,1,3,4]
sol = Solution()
sol.printTree(sol.buildTree(preorder, inorder))

# [1, None, 2, None, 3, None, 4, None, None] == 9
# Output: [1,2,3,None,None,None,4] == 7