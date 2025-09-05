from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def search(root, target):
        if not root:
            return False
        
        if target > root.val:
            return TreeNode.search(root.right, target)
        elif target < root.val:
            return TreeNode.search(root.left, target)
        else:
            return True

    @staticmethod
    def insert(root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = TreeNode.insert(root.right, val)
        elif val < root.val:
            root.left = TreeNode.insert(root.left, val)
        # if val == self.val, do nothing (no duplicates)
        return root

    @staticmethod
    def minValueNode(root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    
    @staticmethod
    def remove(root, val):
        if not root:
            return None 
        
        if val > root.val:
            root.right = TreeNode.remove(root.right, val)
        elif val < root.val:
            root.left = TreeNode.remove(root.left, val)
        else:
            # found the node to be deleted
            if not root.left:
                # no left child
                return root.right
            elif not root.right:
                # no right child
                return root.left
            else:
                # has both children
                minNode = TreeNode.minValueNode(root.right)
                # replace value with inorder successor
                root.val = minNode.val
                # delete the inorder successor
                root.right = TreeNode.remove(root.right, minNode.val)
        return root

    @staticmethod
    def printTree(root):
        if not root:
            print([])
        
        tree = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                tree.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                tree.append(None)
        print(tree)


test = TreeNode(5)
TreeNode.insert(test, 3)
TreeNode.insert(test, 7)
TreeNode.insert(test, 1)
TreeNode.insert(test, 9)
TreeNode.printTree(test)
