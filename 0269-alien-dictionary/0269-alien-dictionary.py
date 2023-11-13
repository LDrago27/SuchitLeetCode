from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        def findOrdering(str1,str2):
            n,m = len(str1),len(str2)
            
            minLen = min(n,m)
            for i in range(minLen):
                if str1[i]!=str2[i]:
                    return (str1[i],str2[i])
                
            # So all elemtns are equal and only thing left is str2
            if n>m:
                return ("-1","-1") # It is not possible so ignore them
            
            if n==m:
                return (str2[n-1],str2[n-1])

            return (str2[n-1],str2[n])
        
        
        graph = defaultdict(list)
        
        n = len(words)
        
        outDegree = {}
        
        for i in range(1,n):
            a,b = findOrdering(words[i-1],words[i])
            if a==b =="-1":
                return ""
            if a==b:
                continue
            graph[b].append(a) # We store backedges i.e from child to parent
            outDegree[a] = outDegree.get(a,0)+1
            outDegree[b] = outDegree.get(b,0)
            
        # Topological Sort
        # Une xplored letters we can just lump them at the end

        res = []
        
        queue = []
        
        # getting the elements with 0 outDegree
        for key in outDegree:
            if outDegree[key] == 0:
                queue.append(key)
                
        while queue:
            newQueue = []
            
            for ele in queue:
                res.append(ele)
                for nextEle in graph[ele]:
                    outDegree[nextEle] -= 1
                    if outDegree[nextEle] == 0:
                        newQueue.append(nextEle)
                        
            queue = newQueue[:]
        
        # Check if it is valid
        for key in outDegree:
            if outDegree[key] > 0:
                return "" # Invalid
            
        # handling elements not in res
        
        res = res[::-1]
        
        for word in words:
            
            for ele in word:
                if ele not in res:
                    res.append(ele)
                    
        return "".join(res)
                    
                
        
        
        
            
