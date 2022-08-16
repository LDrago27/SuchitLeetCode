class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*n for _ in range(m)]
        
        dp[-1] = matrix[-1]
        
        for i in range(m-2,-1,-1):
            for j in range(n):
                tempRes = float('inf')
                
                if j-1>=0:
                    tempRes = min(tempRes,dp[i+1][j-1])
                if j+1<n:
                    tempRes = min(tempRes,dp[i+1][j+1])
                
                dp[i][j] = min(tempRes,dp[i+1][j])+matrix[i][j]
                
        #print(dp)
        return min(dp[0])