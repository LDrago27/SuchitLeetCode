class Solution:
    def countHousePlacements(self, n: int) -> int:
        # Idea is that for each way to place an house on one side we can do the same on other side so answer is dp[n]^2
        
        # place house on side
        
        exp = 10**9+7
        
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2,n+1):
            dp[i] = (dp[i-1] + dp[i-2])%exp
            
        return pow(dp[n],2,exp)
        
        