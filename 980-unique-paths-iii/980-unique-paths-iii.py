class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        res= [0]
        m = len(grid)
        n = len(grid[0])
        
        noZero = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    noZero+=1
        
        def dfs(currNode,visited,ctr):
            #print(currNode)
            x,y = currNode
            
            if grid[x][y] == 2 and ctr==noZero:
                res[0]+=1
                return

            visited[x][y] = True
 
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if abs(dx)==abs(dy) or x+dx>=m or x+dx<0 or y+dy>=n or y+dy<0:
                        continue
                    #print(x+dx,y+dy)
                    if (grid[x+dx][y+dy] ==0 or grid[x+dx][y+dy]==2) and not visited[x+dx][y+dy]:
                        if grid[x+dx][y+dy] == 0:
                            dfs((x+dx,y+dy),visited,ctr+1)
                        else:
                            dfs((x+dx,y+dy),visited,ctr)
            
            visited[x][y] = False
                        
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs((i,j),visited,0)
                    break
        
        return res[0]
        