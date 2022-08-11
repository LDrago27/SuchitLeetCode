class Solution:
    def rob(self, nums: List[int]) -> int:
        # choices at each step we either break into this n house and take max value till n-2 or else not break into this house and take n-1 value
        
        n = len(nums)
        money = [0]*n
        
        if n==1:
            return nums[0]
        
        money[0] = nums[0]
        money[1] = max(nums[1],money[0])
        
        for i in range(2,n):
            money[i] = max(nums[i]+money[i-2],money[i-1])
        
        return money[-1]

            