from collections import defaultdict
from heapq import heapify,heappop,heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visitedNode = set()
        graph = defaultdict(list)
        time = [float('inf')]*(n+1)
        
        for x,y,wt in times:
            graph[x].append([y,wt])
        
        heap = [[0,k]]
        
        time[k] = 0
        time[0] = 0
        
        while heap:
            timeN, node = heappop(heap)
            visitedNode.add(node)
            for nextNode,nextTime  in graph[node]:
                if nextNode not in visitedNode and timeN+nextTime < time[nextNode]:
                    time[nextNode] = timeN + nextTime
                    heappush(heap,[time[nextNode],nextNode])
                    
        res = max(time)
        
        if res == float('inf'):
            return -1
        return res
        