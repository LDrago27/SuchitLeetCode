from heapq import heappop,heapify,heappush
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n,m = len(heights),len(heights[0])
        dist = [[float('inf')] * m for _ in range(n)]
        
        visited = set()
        end = (n-1,m-1)
        
        heap = [[0,(0,0)]]
        
        dist[0][0] = 0
        
        movement = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while heap:
            nodeDist,nodeEle = heappop(heap)
            
            x,y = nodeEle
            if nodeEle == end:
                return nodeDist
            
            visited.add(nodeEle)
            
            for dx,dy in movement:
                newX,newY = x+dx,y+dy
                
                if newX<0 or newX>=n or newY<0 or newY>=m or (newX,newY) in visited:
                    continue
                    
                if dist[newX][newY] > max(nodeDist,abs(heights[x][y]-heights[newX][newY])):
                    dist[newX][newY] = max(nodeDist,abs(heights[x][y]-heights[newX][newY]))
                    
                    heappush(heap,[dist[newX][newY],(newX,newY)])
                    
        
            