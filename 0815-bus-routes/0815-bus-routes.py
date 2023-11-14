from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        #Idea: We will need to use need to use BFS and search on bassis on busroute
        
        # create a inverse map
        
        graph = defaultdict(list)
        
        n = len(routes)
        
        for i in range(n):
            
            for stop in routes[i]:
                graph[stop].append(i)
                
        # Now we have our inverse map
        
        queue = [source]
        dist = 0
        
        seen = set()
        routeSeen = set()
        
        while queue:
            newQueue = []
        
            for stop in queue:
                
                if stop == target:
                    return dist
                if stop in seen:
                    continue
                    
                seen.add(stop)
                
                for bus in graph[stop]:
                    
                    if bus in routeSeen:
                        continue
                    
                    routeSeen.add(bus)
                    
                    for nextStop in routes[bus]:
                        
                        if nextStop in seen:
                            continue
                            
                        newQueue.append(nextStop)
                        
            dist+=1
            queue = newQueue[:]
            
            
        return -1
             
        