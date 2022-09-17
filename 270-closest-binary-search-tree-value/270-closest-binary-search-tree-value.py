# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        minDiff = [float('inf'),-1]
        
        def valueUtil(root,target):
            
            if root == None:
                return
            
            if minDiff[0] > abs(target-root.val):
                minDiff[0] = abs(target-root.val)
                minDiff[1] = root.val
                
            if target-root.val >0:
                return valueUtil(root.right,target)
            elif target-root.val<0:
                return valueUtil(root.left,target)
            else:
                return
        
        valueUtil(root,target)
        return minDiff[1]