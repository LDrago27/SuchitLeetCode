# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # Main thing is the max path may or may not pass through the root
        # Case 1: It terminates left+ root + right or left alone + root , right + root or recurr in the subtree
        # while returning we return a path that include sroot or root 
        
        res = [float('-inf')]
        
        def pathSumUtil(node):
            
            if node == None:
                return float('-inf')
            
            leftValue = pathSumUtil(node.left)
            rightValue = pathSumUtil(node.right)
            
            # updating the global maxima
            # Case1 : Not including the root, not needed since this is already covered by recursive use case
            
            res[0] = max(res[0],node.val,node.val+leftValue,node.val+rightValue,node.val+leftValue+rightValue)
            
            return max(node.val,node.val+leftValue,node.val+rightValue)
        
        pathSumUtil(root)
        return res[0]
            
            