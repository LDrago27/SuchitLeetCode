from heapq import heapify,heappop,heappush
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        #we can use dijkstra algorithm the case is now we need to check intermediate steps too
        #for lexographic ordering we can just move in that order
        
        n,m = len(maze),len(maze[0])
        
        dist = []
        for _ in range(n):
            temp = []
            for i in range(m):
                temp.append([n*m,'z'*(n*m)])
            dist.append(temp)
        visited = set()
        # d,l,r,u
        movement = [[-1,0],[1,0],[0,-1],[0,1]]
        direction = 'udlr'
        heap = [[0,'',ball]]
        dist[ball[0]][ball[1]] = [0,'']
        
        while heap:
            print(heap)
            nodeDist,path,node =  heappop(heap)
            x,y = node
            if node == hole:
                 return path
                
            visited.add((x,y))
            
            for ind,move in enumerate(movement):
                dx,dy = move
                newX,newY = x,y
                
                newDist = 0
                while -1<newX+dx<n and -1<newY+dy<m and maze[newX+dx][newY+dy]!=1:
                    newX+=dx
                    newY+=dy
                    newDist+=1
                    if [newX,newY] == hole:
                        break
                
                print(str(nodeDist+newDist)+path+direction[ind])
                print(str(dist[newX][newY][0])+dist[newX][newY][1])
                
                if (newX,newY) not in visited:
                    dist[newX][newY] = [nodeDist+newDist,path+direction[ind]]
                    heappush(heap,[nodeDist+newDist,path+direction[ind],[newX,newY]])
        return 'impossible'
                    
        
        