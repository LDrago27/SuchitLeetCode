# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        arr = [i for i in range(n+1)]
        
        def createBSTUtil(start,end):
            res = []        
            if start>end:
                return [None]
            
            else:
                for i in range(start,end+1):
                    
                    leftComb = createBSTUtil(start,i-1)
                    rightComb = createBSTUtil(i+1,end)
                    
                    for leftPart in leftComb:
                        for rightPart in rightComb:
                            res.append(TreeNode(arr[i],leftPart,rightPart))
                            
                return res
        return createBSTUtil(1,n)
                    
    
            
            
        