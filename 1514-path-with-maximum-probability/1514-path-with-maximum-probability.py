from heapq import heappop,heapify,heappush
from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = defaultdict(list)
        
        for index,val in enumerate(edges):
            x,y = val
            graph[x].append([y,succProb[index]])
            graph[y].append([x,succProb[index]])
            
            
        heap = [[-1,start]]
        netProb = [float('-inf')]*(n+1)
        
        while heap:
            #print(heap)
            prob, node = heappop(heap)
            prob = prob*-1
            if node ==  end:
                return prob
            
            for ele,edgeProb in graph[node]:
                if netProb[ele] < prob * edgeProb:
                    netProb[ele] = edgeProb*prob
                    heappush(heap,[-netProb[ele],ele])
        
        if netProb[end] ==  float('-inf'):
            return 0