# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root  == None:
            return True
        
        def isEqual(root1,root2):
            if root1 == root2 == None:
                return True
            elif root1 == None:
                return False
            elif root2 == None:
                return False
            
            if root1.val == root2.val:
                return isEqual(root1.left,root2.right) and isEqual(root1.right,root2.left)
            
            return False
            
        if root.left == None and root.right == None:
            return True
        elif root.left == None:
            return False
        elif root.right == None:
            return False
        return isEqual(root.left,root.right)
        
            