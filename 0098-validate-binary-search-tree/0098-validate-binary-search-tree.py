# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxTree(self, root):
        if root is None:
            return float('-inf')
        else:
            return max(root.val,self.maxTree(root.left),self.maxTree(root.right))
    def minTree(self, root):
        if root is None:
            return float('inf')
        return min(root.val,self.minTree(root.left),self.minTree(root.right))

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        else:
            if root.val > self.maxTree(root.left) and root.val<self.minTree(root.right):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            return False

