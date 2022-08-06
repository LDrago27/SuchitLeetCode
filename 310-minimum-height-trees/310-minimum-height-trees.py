from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # atmost we can have 2 MHT i.e pick up the root somewhere in middle of the graph to keep the edges balanced
        # how do we pick up the root we can use the conecpt of outdegree we can start by eliminating nodes with out degree of 1 at each step till have either 1 or 2 nodes in the graph
        
        
        graph = defaultdict(list)
        inDegree = [0]*n
        
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
            inDegree[start]+=1
            inDegree[end]+=1
        
        queue = []
        noElement = n
        for i in range(n):
            if inDegree[i] ==1:
                queue.append(i)
        if n==1:
            return [0]
        elif n==0:
            return []
        
        while noElement > 2:
            new_queue = []
            noElement-=len(queue)
            
            while queue:
                node = queue.pop(0)
                inDegree[node]-=1
                
                for neighbour in graph[node]:
                    graph[neighbour].remove(node)
                    inDegree[neighbour]-=1
                    if inDegree[neighbour] == 1:
                        new_queue.append(neighbour)
                
                graph[node] = []
            queue = new_queue
        
        return queue
            
        
            
            
            
        