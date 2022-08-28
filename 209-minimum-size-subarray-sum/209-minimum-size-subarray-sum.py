class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tempSum = 0
        start = 0
        end = 0
        n = len(nums)
        res = float('inf')
        
        while end<n:
            tempSum+=nums[end]
            
            while start<=end and tempSum>=target:
                res = min(end-start+1,res)
                tempSum-=nums[start]
                start+=1
            
            end+=1
        if res == float('inf'):
            return 0
        return res
        
                
            