from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
         # if cyclic then -1
            # can use a concept similar to BFS to find min distance to reach the last course
            # how to find the start course and end course in BFS
            # Quite close just run a multi source BFS using nodes with no inDegree
            
            visited = [False]*(n+1)
            graph = defaultdict(list)
            inDegree = [0]*(n+1)
            
            for x,y in relations:
                graph[x].append(y)
                inDegree[y]+=1
            
            queue = []
            for i in range(1,n+1):
                if not inDegree[i]:
                    queue.append(i)
            
            level = 0
            
            visitedELe = 0
            
            while visitedELe<n+1 and queue:
                newQueue = []
                level+=1
                
                while queue:
                    node = queue.pop(0)
                    visited[node] = True
                    visitedELe+=1
                    
                    inDegree[node]-=1

                    for neighbour in graph[node]:
                        inDegree[neighbour]-=1
                        if inDegree[neighbour] ==0:
                            newQueue.append(neighbour)
                
                queue = newQueue.copy()
            if visitedELe == n:
                return level
            return -1
            
            
                        