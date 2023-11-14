class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Multi source BFS it will give nearest distance of each one Element
        
        queue = []
        n,m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                
                if mat[i][j] == 0:
                    queue.append([(i,j),0])
        seen = set([])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while queue:
            node, dist = queue.pop(0)
            
            x,y = node
            
            if node in seen:
                continue
                
            seen.add(node)
            
            if mat[x][y] !=0:
                mat[x][y] = dist
                
            for dx,dy in directions:
                newX,newY = x+dx, y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or mat[newX][newY]==0 or (newX,newY) in seen:
                    continue
                    
                queue.append([(newX,newY),dist+1])
        
        return mat
            
            