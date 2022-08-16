class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        m = 3
        
        dp = [[0]*m for _ in range(n)]
        
        dp[0] = costs[0]
        # dp(i,j) -> means we are using i with color j what min is required
        for i in range(1,n):
            for j in range(3):
                tempRes = float('inf')
                for  k in range(3):
                    if k==j:
                        continue
                    tempRes = min(tempRes,dp[i-1][k])
                dp[i][j] = tempRes + costs[i][j]
        
        return min([dp[-1][j] for j in range(3)])