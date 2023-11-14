class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        #dist = {} # mapping of water coordinates -> nearest distance from any land mass
        
        # Since we need the shortest disance from any land mass we can make use of Multi Source BFS
        
        queue = []
        
        n,m = len(grid), len(grid[0])
        water = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append([(i,j),0])
                else:
                    water += 1
        
        # Basic unit of manhattand distance can be 1 , hence the cells are connected by 4 directions
        directions = [[0,1],[0,-1],[1,0],[-1,0]]    
        seen = set([])
        while queue:
            
            node,dist = queue.pop(0)
            
            if node in seen:
                continue
                
            seen.add(node)
            x,y = node
            
            if grid[x][y] == 0:
                water-=1
                if water == 0:
                    return dist
            
            for dx,dy in directions:
                newX,newY = x+dx, y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or (newX,newY) in seen or grid[newX][newY]==1:
                    continue
                
                queue.append([(newX,newY),dist+1])
                
        return -1