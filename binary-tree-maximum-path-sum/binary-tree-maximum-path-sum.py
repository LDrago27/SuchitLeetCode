# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 2 Scenarios : 
        # either end at the given node as root else return back to its parent
        
        res = [float('-inf')]
        
        def maxPathUtil(root):
            if root == None:
                return 0
            
            # Case1 end at the given node
            maxLeftValue = maxPathUtil(root.left)
            maxRightValue =  maxPathUtil(root.right)
            
            case1Res = max(root.val,root.val+ maxLeftValue + maxRightValue, root.val + max(maxLeftValue,maxRightValue))
            
            res[0] = max(res[0],case1Res)
            
            #Case2 Value
            # either return alone or with the left or right part
            return max(root.val,root.val + max(maxLeftValue,maxRightValue))
            
        maxPathUtil(root)
        return res[0]
        
            