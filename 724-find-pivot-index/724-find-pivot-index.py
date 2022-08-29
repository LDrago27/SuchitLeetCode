class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        netSum = sum(nums)
        
        n = len(nums)
        tempSum = 0
        
        for i in range(n):
            
            if tempSum == (netSum - tempSum -nums[i]):
                return i
            
            tempSum+= nums[i]
        return -1
                        