# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None:
            return None
        
        if root == p or root==q:
            return root
        
        lval = self.lowestCommonAncestor(root.left,p,q)
        rval = self.lowestCommonAncestor(root.right,p,q)
        
        if lval and rval:
            return root
        elif lval:
            return lval
        elif rval:
            return rval
        return None