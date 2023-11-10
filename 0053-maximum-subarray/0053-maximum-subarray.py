class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane
        
        temp,res = 0,max(nums)
        
        for ele in nums:
            temp += ele
            res = max(res,temp)
            if temp < 0:
                temp = 0
        return res
