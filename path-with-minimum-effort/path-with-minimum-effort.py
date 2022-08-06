from heapq import heappush,heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n = len(heights)
        m = len(heights[0])
        
        minDist = [[float('inf')]*m for _ in range(n)]         
        minDist[0][0] = 0
        
        res = float('inf')
        
        visited = set()
        heap = [[0,0,0]]
        
        while heap:
            effort,x,y = heappop(heap)
            
            visited.add((x,y))
                
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if abs(dx) == abs(dy):
                        continue
                    
                    newX = x+dx
                    newY = y+dy
                    
                    if newX>=n or newX<0 or newY<0 or newY>=m or (newX,newY) in visited :
                        continue
                    
                    newEffort = abs(heights[x][y]-heights[newX][newY])
                    effortUpdate = max(effort,newEffort)

                    if effortUpdate < minDist[newX][newY]:
                        minDist[newX][newY] = effortUpdate 
                        heappush(heap,[effortUpdate,newX,newY])
        #print(minDist)
        return minDist[-1][-1]