# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def maxValue(root):
            if root == None:
                return float('-inf')
            return max(root.val,maxValue(root.left),maxValue(root.right))
        
        def minValue(root):
            if root == None:
                return float('inf')
            return min(root.val,minValue(root.left),minValue(root.right))
        
        if root == None:
            return True
        
        if root.left == None and root.right == None:
            return True
        
        if root.val > maxValue(root.left) and root.val< minValue(root.right):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        return False
    
        