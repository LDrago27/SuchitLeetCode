class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        movement = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(node,groupId):
            
            x,y = node[0],node[1]
            grid[x][y] = str(groupId)
            
            for dx,dy in movement:
                newX,newY = x+dx,y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or grid[newX][newY]!='1':
                    continue
                
                dfs((newX,newY),groupId)
        
        groupId = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs((i,j),groupId)
                    groupId+=1
        
        return groupId -2
            
        