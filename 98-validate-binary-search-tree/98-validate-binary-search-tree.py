# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def findMin(root):
            if root == None:
                return float('inf')
            return min(root.val,findMin(root.left),findMin(root.right))

        def findMax(root):
            if root == None:
                return float('-inf')
            return max(root.val,findMax(root.left),findMax(root.right))

        def isValidUtil(root):
            
            if  root == None or root.right == None and root.left == None:
                return True
            if root.val > findMax(root.left) and root.val< findMin(root.right):
                return isValidUtil(root.left) and isValidUtil(root.right)
            return False
        return isValidUtil(root)
            