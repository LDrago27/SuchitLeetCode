
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = []
        fresh = 0
        
        n,m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                
                if grid[i][j] == 2:
                    queue.append([(i,j),0])
                elif grid[i][j]==1:
                    fresh+=1
                    
        seen = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while queue:
            node,time = queue.pop(0)
            
            if node in seen:
                continue
                
            seen.add(node)
            x,y = node
            
            if grid[x][y] == 1:
                fresh-=1
                grid[x][y] = 2
            
            if fresh == 0:
                return time
            
            for dx,dy in directions:
                newX,newY = x+dx,y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or grid[newX][newY] !=1:
                    continue
                
                queue.append([(newX,newY),time+1])
                
            
            
        if fresh == 0:
            return 0
        else:
            return -1