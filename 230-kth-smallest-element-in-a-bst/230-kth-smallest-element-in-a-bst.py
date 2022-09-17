# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def kSmallUtil(root,k):
            if k == 0:
                return [root,0]
            if k>0 and root == None:
                return [None,k]
            
            leftSide = kSmallUtil(root.left,k)
            if leftSide[0]!=None:
                return [leftSide[0],0]
            else:
                remain = leftSide[1]
                if remain ==1:
                    return [root,0]
                return kSmallUtil(root.right,remain-1)
        
        return kSmallUtil(root,k)[0].val
            
            
            
            