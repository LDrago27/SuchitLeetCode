from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS algorithm
        
        origColor =  image[sr][sc]
        if origColor == color:
            return image
        
        n = len(image)
        m = len(image[0])
        
        visited = set((sr,sc))
        queue = deque([(sr,sc)])
        movement = [[-1,0],[1,0],[0,1],[0,-1]]
        image[sr][sc] = color
        
        while queue:
            x,y = queue.popleft()
            
            for dx,dy in movement:
                newX,newY = dx+x,y+dy
                if newX<0 or newY<0 or newX>=n or newY>=m or image[newX][newY]!=origColor or (newX,newY) in visited :
                    continue
                queue.append((newX,newY))
                visited.add((newX,newY))
                image[newX][newY] = color
        return image
                
                
            
            
            