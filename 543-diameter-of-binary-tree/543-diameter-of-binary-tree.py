# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy  
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = []
        maxPathLen = [0]
        
        def maxPathUtil(root):
            if root == None:
                return []
            
            leftSideMaxPath = maxPathUtil(root.left)
            rightSideMaxPath = maxPathUtil(root.right)
            
            if len(leftSideMaxPath)+len(rightSideMaxPath)+1> maxPathLen[0]:
                temp = leftSideMaxPath[::-1]+[root.val]+rightSideMaxPath
                if res:
                    res.pop()
                res.append(temp)
                maxPathLen[0] = len(leftSideMaxPath)+len(rightSideMaxPath)+1
                
            if len(leftSideMaxPath) > len(rightSideMaxPath):
                return [root.val]+leftSideMaxPath
            else:
                return [root.val]+rightSideMaxPath
        maxPathUtil(root)
        print(res)
        return maxPathLen[0]-1