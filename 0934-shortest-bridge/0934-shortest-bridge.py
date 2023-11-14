class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        # Identify the island and mark the grids as 1 and 2 
        
        # We can either use union find to DFs to do it, we will use DFS
        
        seen = set()
        
        n,m = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        
        def dfs(node,color):
            
            x,y = node
            seen.add(node)
            grid[x][y] = color
            for dx,dy in directions:
                newX,newY = x+dx, y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or grid[newX][newY]!=1 or (newX,newY) in seen:
                    continue
                    
                dfs((newX,newY),color)
        
        color = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and (i,j) not in seen:
                    dfs((i,j),color)
                    color+=1
        
        # Now we have 2 colored island one marked 1 and another marked 2 now we need to use multisource DFS 
        # From all the eellements of island 1 until we find a element of island 2
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append([(i,j),0])
                    
        seen = set([])
        
        while queue:
            node,dist = queue.pop(0)
            
            if node in seen:
                continue
            
            seen.add(node)
            x,y = node
            
            if grid[x][y] == 2:
                return dist-1
            
            for dx,dy in directions:
                newX,newY = x+dx,y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or (newX,newY) in seen or grid[newX][newY]==1:
                    continue
                    
                queue.append([(newX,newY),dist+1])
                
        
        
        