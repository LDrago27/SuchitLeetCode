class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        # Upper Limit We will populate for each of the
        n = len(grid)
        colWise,rowWise = [(float('-inf'),-1)]*n,[(float('-inf'),-1)]*n

        
        for i in range(n):
        
            for j in range(n):
                if grid[i][j] > colWise[j][0]:
                    colWise[j] = (grid[i][j],i)
                if grid[i][j] > rowWise[i][0]:
                    rowWise[i] = (grid[i][j],j)
                
        # just based on each of the view try to fix the limit
        maxGrid = [[(float('inf'))]*n for _ in range(n)]
        
        for col in range(n):
            maxValue, index = colWise[col]
            
            for i in range(n):
                maxGrid[i][col] = min(maxValue,maxGrid[i][col])
                
                
        for row in range(n):
            maxValue, index = rowWise[row]
            
            for j in range(n):
                maxGrid[row][j] = min(maxValue,maxGrid[row][j])

        res = 0
        
        for i in range(n):
            for j in range(n):
                res += maxGrid[i][j]-grid[i][j]
        
        return res
                
        
        
                
                
        
                
