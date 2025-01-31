# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None or root == p or root == q:
            return root
        
        leftAncestor = self.lowestCommonAncestor(root.left,p,q)
        rightAncestor = self.lowestCommonAncestor(root.right,p,q)

        if leftAncestor and rightAncestor:
            return root
        elif leftAncestor:
            return leftAncestor
        return rightAncestor 

        