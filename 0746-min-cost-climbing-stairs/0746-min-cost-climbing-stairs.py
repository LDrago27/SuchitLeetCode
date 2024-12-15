class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        dp[0] = dp[1] = 0 # Since we can either start from index 0 or index 1 so the cost of reaching here is 0 
        
        for i in range(2,n+1):
                    
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
            
        return dp[-1]