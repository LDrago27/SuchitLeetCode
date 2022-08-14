class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #square a cool properyty length, breadth and diagonla elelmets nees to be square
        # so basically we build it up
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    matrix[i][j] = 1
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
        
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = matrix[i][0]
            
        for j in range(n):
            dp[0][j] = matrix[0][j]
                
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        
        return max([max(row) for row in dp])*max([max(row) for row in dp])
