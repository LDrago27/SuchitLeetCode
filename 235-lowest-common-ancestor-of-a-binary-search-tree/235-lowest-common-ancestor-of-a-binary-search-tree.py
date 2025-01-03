# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #print(root.val)
        if root == None:
            return root
        
        if p.val<=root.val and root.val<=q.val or (q.val<=root.val and root.val<=p.val):
            return root
        elif root.val >p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)