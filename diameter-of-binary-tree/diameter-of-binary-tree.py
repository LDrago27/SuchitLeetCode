# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            if root == None:
                return 0
            return 1 + max(height(root.left),height(root.right))

        def util(root):
            if root == None:
                return 0

            currHt = height(root.left)+height(root.right)
            return max(currHt,util(root.right),util(root.left))
        
        return util(root)