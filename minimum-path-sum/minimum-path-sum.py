class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m= len(grid)
        n = len(grid[0])
       
        dp = [[0]*n for _ in range(m)]
        
        dp[-1][-1] = grid[-1][-1]
        
        for i in range(m-2,-1,-1):
            dp[i][-1] = grid[i][-1]+dp[i+1][-1]
        
        for j in range(n-2,-1,-1):
            dp[-1][j] = grid[-1][j]+dp[-1][j+1]
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = grid[i][j]+ min(dp[i+1][j],dp[i][j+1])
        
        return dp[0][0]