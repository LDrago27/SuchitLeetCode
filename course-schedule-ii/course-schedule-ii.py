from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        #inDegreeGraph = defaultdict(list)
        inDegree = {}
        for i in range(numCourses):
            inDegree[i] = 0
        
        queue = []
        
        res = []
        
        for x,y in prerequisites:
            graph[y].append(x)
            #inDegreeGraph[y].append(x)
            
            inDegree[x]+=1
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                
                
        while queue:
            ele = queue.pop(0)
            res.append(ele)
            # Remove this Node so delete all elemest who have ele as the parent and decrease their inDegree
            
            for nextEle in graph[ele]:
                inDegree[nextEle]-=1
                
                if inDegree[nextEle] == 0:
                    queue.append(nextEle)
        
        for i in range(numCourses):
            if inDegree[i]!=0:
                return []
        return res