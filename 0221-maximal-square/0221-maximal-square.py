class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Idea is first condesne along one axis then find another axis
        # This is correct but for maximal rectangles
        # For maximal square we need additional constraints we count only those sqaure where ht == width
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]

        for i in range(n):
            if matrix[0][i] == "1":
                dp[0][i] = 1

        # init the first row
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                else:
                    dp[i][j] = dp[i-1][j]+1
        
        # Now for each element we will try exapanding towards the right to find the max value that we can 
        maxArea = 0
        for i in range(m):
            for j in range(n):
                
                endCol = j
                ht = float('inf')
                
                while endCol<n and dp[i][endCol]:
                    ht = min(ht, dp[i][endCol])
                    if ht == endCol-j+1: # Additional Constrtaint to ensure it is only computed for Squares
                        maxArea = max(maxArea,ht*(endCol-j+1))
                    endCol+=1
                
                
        return maxArea
            