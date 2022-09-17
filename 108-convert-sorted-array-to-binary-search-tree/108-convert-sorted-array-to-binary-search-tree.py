# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createBSTUtil(start,end):
            
            if start>end:
                return None
            
            mid  = (start+end)//2
            return TreeNode(nums[mid],createBSTUtil(start,mid-1),createBSTUtil(mid+1,end))
        
        n = len(nums)
        return createBSTUtil(0,n-1)
            
            
            