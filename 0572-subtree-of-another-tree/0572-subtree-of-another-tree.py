# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isEqual(self, root1, root2):
        if root1 == root2 == None:
            return True
        elif root1 is None:
            return False
        elif root2 is None:
            return False
        else:
            if root1.val!=root2.val:
                return False
            return self.isEqual(root1.left,root2.left) and self.isEqual(root2.right, root1.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == subRoot == None:
            return True
        elif root is None:
            return False
        elif subRoot is None:
            return True # None is always a subRoot
        else:
            if self.isEqual(root,subRoot):
                return True
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)