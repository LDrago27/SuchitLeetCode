class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = [0]
        
        # we will use dfs to visit all paths
        # two concepts start node will always be included and we can loop through all possible startNodes
        # Optimization instead of strating at all nodes we will only start from nodes with 1/2 connections snce other are connected we can pass by them anyways
        
        m = len(grid)
        n = len(grid[0])
        
        def dfsUtil(currNode,visited,pathSum):
            
            visited.add(currNode)
            x,y = currNode
            #print(currNode)
            maxGold[0] = max(maxGold[0],pathSum+grid[x][y])
            
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if abs(dx) == abs(dy) or x+dx>=m or y+dy>=n or x+dx<0 or y+dy<0 or grid[x+dx][y+dy]==0:
                        continue
                    if (x+dx,y+dy) not in visited:
                        dfsUtil((x+dx,y+dy),visited,pathSum+grid[x][y])
            
            visited.remove(currNode)
        
        def isConnectedCells(i,j):
            count = 0
            if i+1 <m and grid[i+1][j]!=0:
                count+=1 
            if j+1<n and grid[i][j+1]!=0:
                count+=1
            if i-1>=0 and grid[i-1][j]!=0:
                count+=1
            if j-1>=0 and grid[i][j-1]!=0:
                count+=1
            return count

        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0 and isConnectedCells(i,j)<=2:
                    visited = set()
                    dfsUtil((i,j),visited,0)
                
        return maxGold[0]
                    
        
        