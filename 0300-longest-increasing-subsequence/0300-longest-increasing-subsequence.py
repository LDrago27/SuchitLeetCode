from heapq import heappop,heappush
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n # themseleves
        
        # For each current value we need find elememts  smaller than it increment it
        # O(n^2) -> Time space O(n)
        for i in range(1,n):
            temp = dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp,dp[j]+1)
            dp[i] = max(dp[i],temp)
        
        return max(dp)
            
                
        