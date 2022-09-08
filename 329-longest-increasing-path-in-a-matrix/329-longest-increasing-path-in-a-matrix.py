class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # brute force start at eac nodde and then just trraverse and store the length
        
        n,m = len(matrix),len(matrix[0])
        
        visited= [[False]*m for _ in range(n)]
        movement = [[-1,0],[1,0],[0,1],[0,-1]]
        res = [0]
        
        cache = {}
        
        def pathLen(currNode,path):
            
            x,y = currNode
            visited[x][y] = True
            path =  1+path
            currVal = matrix[x][y]
            
            temp =0
            for dx,dy in movement:
                newX,newY = x+dx,y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or matrix[newX][newY]<=currVal:
                    continue
                
                if (newX,newY) in cache:
                    temp = max(temp,cache[(newX,newY)])
                
                else:
                    temp = max(temp,pathLen((newX,newY),0))
            #print(temp,path)
            cache[(x,y)] = temp+path
            res[0] = max(res[0],cache[(x,y)])
            return cache[(x,y)]
            
            
        
        
        
        for i in range(n):
            for j in range(m):
                
                if not visited[i][j]:
                    pathLen((i,j),0)
        
        return res[0]
        
        