class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def search(root, target):
        if not root:
            return False
        
        if target > root.val:
            return search(root.right, target)
        elif target < root.val:
            return search(root.left, target)
        else:
            return True