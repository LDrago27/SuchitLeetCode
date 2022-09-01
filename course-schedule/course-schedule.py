from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # so we have a directed graph so if there is an infinte loop or a cycle we have the issue
        # since it is undirected wer will use 
        
        visited =[False]*(numCourses)
        graph = defaultdict(list)
        
        for a,b in prerequisites:
            graph[a].append(b)
        
        def dfs(ele,path):
            
            visited[ele] = True
            path.add(ele)
            
            for neighbour in graph[ele]:
                if neighbour in path:
                    return True
                if not visited[neighbour] and dfs(neighbour,path):
                    return True
            
            path.remove(ele)
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i,set()):
                    return False
        
        return True
            
            
        