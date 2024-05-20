class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
         
        # Idea: WE will use Depth First Search instead of Breadth first search since we need all the paths and not the ppath with minimum distance
        
        # DFs -> per pass O(V+E) from a single starting node -> O(n**2)
        # Read Carefully: Need to traverse each empty space atleast once
        m,n = len(grid), len(grid[0])
        
        res = [0]
        movement = [[1,0],[-1,0],[0,1],[0,-1]]
        
        startNode = (0,0)
        emptyNode = 0
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    startNode = (i,j)
                elif grid[i][j] == 0:
                    emptyNode+=1
        
        def explorePath(currNode, visitedStack):
            x,y=currNode
            
            if grid[x][y] == 2:
                if emptyNode == len(visitedStack) -2:
                    res[0]+=1
                return 
            
            for dx,dy in movement:
                newX,newY = x+dx, y+dy
                
                if newX<0 or newX>=m or newY<0 or newY>=n or (newX,newY) in visitedStack or grid[newX][newY]==-1:
                    continue
                
                visitedStack.add((newX,newY)) # Startting the exploration
                explorePath((newX,newY), visitedStack )
                
                # Reseting the exploration 
                visitedStack.remove((newX,newY))
        

        
        visitedStack = set([startNode])
        print(visitedStack)
        explorePath(startNode, visitedStack)
        return res[0]
    
                
                
                
                
                
                
                
                    