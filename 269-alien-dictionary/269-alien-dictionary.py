from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        n = len(words)
        
        graph = defaultdict(list)
        
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = []
        
        def returnOrder(s1,s2):
            minN = min(len(s1),len(s2))
            mismatchIndex = -1
            
            for i in range(minN):
                if s1[i]!=s2[i]:
                    mismatchIndex = i
                    break
                    
            if  s1[:minN]==s2[:minN] and len(s1) > len(s2):
                return ('-1','-1')
            elif mismatchIndex == -1:
                return ('','')
            
            return (s1[i],s2[i])
        
        
        for i in range(n-1):            
            x,y = returnOrder(words[i],words[i+1])
            if x == '':
                continue
            elif x == '-1':
                return ""
            else:
                graph[x].append(y)
        
        stack = []
        
        print(graph)
        
        def topologicalSortUtil(currNode,visited,inCycle):
            # return True if there is a cycle
            visited.add(currNode)
            
            for neighbour in graph[currNode]:
                if neighbour not in visited:
                    if (topologicalSortUtil(neighbour,visited,inCycle+[currNode])):
                        return True
                if neighbour in inCycle:
                    return True
            if currNode not in stack:
                stack.append(currNode)
            return False
                
        startNode =[0]
        
        visited = set()
        
        for startNode in list(graph.keys()):
            if startNode not in visited:            
                 if topologicalSortUtil(startNode,visited,[]):
                        return ''
        
        return ''.join(stack[::-1])
            
            
            
        