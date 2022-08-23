class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        
        for i in range(n):
            maxEle = nums[i]
            minEle = nums[i]
            
            for j in range(i+1,n):
                maxEle = max(maxEle,nums[j])
                minEle = min(minEle,nums[j])
                res+= maxEle - minEle
        
        return res