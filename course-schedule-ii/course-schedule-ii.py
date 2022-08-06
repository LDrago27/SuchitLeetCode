from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # topological sorting bascially for every edge u->v u comoes before v
        # similar to dfs or more appropriately preorder tree traversal
        
        graph = defaultdict(list)
        
        for [a,b] in prerequisites:
            graph[b].append(a)
            
        visited = [False]*(numCourses)
        stack = []
        isCyclic = [False]
        
        def topologicalSortUtil(node,stack,visitedInCycle):
            visited[node] = True
            #print(node,visitedInCycle)
            for neighbour in graph[node]:
                if neighbour in visitedInCycle:
                    #Cyclic so none
                    isCyclic[0] = True
                    return
                if not visited[neighbour]:
                    topologicalSortUtil(neighbour,stack,visitedInCycle+[node])
            
            stack.append(node)
            
        for i in range(numCourses):
            if not visited[i]:
                topologicalSortUtil(i,stack,[])
        if isCyclic[0]:
            return []
        return stack[::-1]

        