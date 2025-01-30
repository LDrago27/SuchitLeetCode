# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [float('-inf')]

        cache = {}

        def pathWithRootMax(root):
            if root in cache:
                return cache[root]

            if root is None:
                return 0

            # Case 1: Either current root or root + left side or root+ right Side, or root + right + left side

            returnVal = max(root.val, root.val+pathWithRootMax(root.left), root.val + pathWithRootMax(root.right))

            res[0] = max(res[0],root.val + pathWithRootMax(root.right) + pathWithRootMax(root.left),returnVal)
            # root.val + pathWithRootMax(root.right) + pathWithRootMax(root.left) -> It is ending the section so we can't really end it here
            cache[root] = returnVal
            return returnVal
        
        pathWithRootMax(root)
        return res[0]
        