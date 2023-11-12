class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        
        # At each house either rob it or not
        
        # Case 1 We rob it on day 1
        # No choice for last day
        if n==1:
            return nums[0]
        
        dp[0] = nums[0]
        dp[1] = nums[0]
        for i in range(2,n-1):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            
        res = max(dp)
        
        
        # Case 2 We don't rob it on day 1
        dp = [0]*n
        
        for i in range(1,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])

        return max(res,max(dp))
        