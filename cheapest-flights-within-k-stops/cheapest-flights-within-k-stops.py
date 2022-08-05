from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # we can use a modified version of dijkstra that will have a overall limit of k turns
        # similar to bfs levels
        
        graph = defaultdict(list)
        
        for frm,to,price in flights:
            # instead to storing parent ->child relationship we will store it in reverse
            graph[to].append([frm,price])
        
        prevDist = [float('inf')]*n
        currDist = [float('inf')]*n
        
        prevDist[src] = 0
        currDist[src] = 0
        
        for j in range(1,k+2):
            for i in range(n):
                minCost = float('inf')

                if i==src:
                    continue
                
                for parent,dist in graph[i]:
                    minCost = min(minCost,prevDist[parent]+dist)
                
                currDist[i] = min(minCost,prevDist[i])
            prevDist = currDist.copy()
            print(currDist)
        if currDist[dst] == float('inf'):
            return -1
        return currDist[dst]
                
                
                
                
            
            
            
            
        
        
       
        