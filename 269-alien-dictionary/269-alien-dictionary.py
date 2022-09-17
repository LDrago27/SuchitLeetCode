from collections import defaultdict,OrderedDict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = defaultdict(list)
        
        inDegree = OrderedDict()
        
        def findDifferChar(s1,s2):
            
            n1,n2 = len(s1),len(s2)
            
            maxInd = min(n1,n2)
            
            for i in range(maxInd):
                if s1[i] != s2[i]:
                    return [s1[i],s2[i],i]
            
            return []
        
        n = len(words)
        if n==1:
            return ''.join(list(set(words[0])))
        
        for i in range(n-1):
            val =  findDifferChar(words[i],words[i+1])
            
            
            
            if len(val)==0:
                for char in words[i]:
                    inDegree[char] = inDegree.get(char,0)
                for char in words[i+1]:
                    inDegree[char] = inDegree.get(char,0)
                
                if len(words[i+1]) < len(words[i]):
                    return ''
                continue
            
            graph[val[0]].append(val[1])
            
            inDegree[val[0]] = inDegree.get(val[0],0)
            inDegree[val[1]] = inDegree.get(val[1],0)+1
            
            if val[2]!=0:
                for char in words[i][:val[2]]:
                    inDegree[char] = inDegree.get(char,0)
            if val[2]+1 < len(words[i]):
                for char in words[i][val[2]+1:]:
                    inDegree[char] = inDegree.get(char,0)
            if val[2]+1 < len(words[i+1]):
                for char in words[i+1][val[2]+1:]:
                    inDegree[char] = inDegree.get(char,0)
            
        # now we need a topological sort
        
        res = []
        keyList = list(inDegree.keys())
        queue = []
        
        for key in keyList:
            if inDegree[key] == 0:
                queue.append(key)
        
        while queue:
            ele = queue.pop(0)
            res.append(ele)
            for nextEle in graph[ele]:
                inDegree[nextEle]-=1
                
                if inDegree[nextEle] == 0:
                    queue.append(nextEle)
        
        for key in keyList:
            if inDegree[key]!=0:
                return ''
            
        return ''.join(res)
            
            
        