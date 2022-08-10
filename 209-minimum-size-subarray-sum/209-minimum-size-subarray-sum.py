class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2 3 1 2 4 3
        # 2 5 6 8 12 15
        n = len(nums)
        leftSideSum = [0]*n
        leftSideSum[0] = nums[0]
        
        for i in range(1,n):
            leftSideSum[i] = nums[i]+leftSideSum[i-1]
        
        start = 0 
        end = 0
        
        res = float('inf')
        
        while end<n and start<=end:
            
            if leftSideSum[end]-leftSideSum[start]+nums[start]>= target:
                res = min(res,end-start+1)
                start+=1
            
            else:
                end+=1
        
        if res == float('inf'):
            return 0
        return res
        
        