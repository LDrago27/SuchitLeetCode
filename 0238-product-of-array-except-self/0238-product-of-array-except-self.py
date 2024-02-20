class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # have 2 arrays left hand Prod and Right Side prod exluding the curr Element
        n = len(nums)
        leftSide = [1]*n
        rightSide = [1]*n
        
        for i in range(1,n):
            leftSide[i] = leftSide[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            rightSide[i] = rightSide[i+1]*nums[i+1]
            
        res = []
        
        for i in range(n):
            res.append(leftSide[i]*rightSide[i])
            
        return res
        