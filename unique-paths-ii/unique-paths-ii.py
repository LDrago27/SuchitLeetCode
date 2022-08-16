class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m  = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        if obstacleGrid[-1][-1]:
            return 0
        dp[-1][-1] = 1
        
        for i in range(m-2,-1,-1):
            if obstacleGrid[i][-1]:
                break
            dp[i][-1] = 1
            
        for j in range(n-2,-1,-1):
            if obstacleGrid[-1][j]:
                break
                
            dp[-1][j] =1
            
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i+1][j]+dp[i][j+1]
        
        return dp[0][0]
        