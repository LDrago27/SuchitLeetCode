class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        numIsland = 2
        
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False]*m for _ in range(n)]
        
        
        def dfs(i,j,IslandNumber):
            
            if i >=n or i<0 or j>=m or j<0 or grid[i][j] == "0" or visited[i][j]:
                return
            
            visited[i][j] = True
            grid[i][j] = IslandNumber
            
            dfs(i+1,j,IslandNumber)
            dfs(i,j+1,IslandNumber)
            dfs(i-1,j,IslandNumber)
            dfs(i,j-1,IslandNumber)
            
        for i in range(n):
            for j in range(m):
                if visited[i][j] == False and grid[i][j] == "1":
                    dfs(i,j,numIsland)
                    numIsland+=1
        
        return numIsland-2
            
            
            
        