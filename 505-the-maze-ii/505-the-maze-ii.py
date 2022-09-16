from heapq import heapify,heappush,heappop
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        visited = set()
        dist = [[float('inf')]*m for _ in range(n)]
        
        heap = [[0,start]]
        
        dist[start[0]][start[1]] == 0
        
        movement = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while heap:
            nodeDist, currNode = heappop(heap)
            x,y =  currNode
            
            if currNode == destination:
                return nodeDist
            
            visited.add((x,y))
            
            for dx,dy in movement:
                newX,newY = x,y
                newDist = 0
                while -1<newX+dx<n and -1<newY+dy<m and maze[newX+dx][newY+dy]!=1:
                    newX +=dx
                    newY +=dy
                    newDist+=1
                    
                
                # stopping cooridinates newX,newY
                
                if (newX,newY) not in visited and dist[newX][newY] > nodeDist+newDist:
                    dist[newX][newY] = nodeDist+newDist
                    heappush(heap,[dist[newX][newY],[newX,newY]])
        
        return -1
                
                    
                