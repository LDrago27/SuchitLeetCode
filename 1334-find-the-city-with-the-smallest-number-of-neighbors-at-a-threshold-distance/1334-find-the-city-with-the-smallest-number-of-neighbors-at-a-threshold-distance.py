from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        # naive idea run dijstra on each node and remove ciity with cutoff
        

        
        graph = defaultdict(list)
        
        for x,y,wt in edges:
            graph[x].append([y,wt])
            graph[y].append([x,wt])
        
        minCity = float('inf')
        minCityIndex = -1
        
        for i in range(n-1,-1,-1):
            
            visited = set()
            #print(visited)
            dist = [float('inf')]*n
            heap = [[0,i]]
            dist[i] = 0
            
            while heap:
                nodeDist,nodeEle = heappop(heap)
                
                visited.add(nodeEle)                
                for nextEle,wt in graph[nodeEle]:
                    if dist[nextEle]> wt+nodeDist and nextEle not in visited:
                        dist[nextEle] = wt+nodeDist
                        heappush(heap,[dist[nextEle],nextEle])
                
            tempMin = 0
            for j in range(n):
                if i!=j and dist[j]<=distanceThreshold:
                    tempMin+=1
            #print(i,tempMin,dist)
            if tempMin < minCity:
                minCity= tempMin
                minCityIndex = i
                
        return minCityIndex
            
        
        