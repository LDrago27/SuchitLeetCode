from collections import defaultdict
class Solution:
    
    def topologicalOrdering(self, edgeSet, allCharSet):
        # Kahn Algorithm
        inDegree = {}

        adjList = defaultdict(list)

        for x,y in edgeSet:
            if (y,x) in edgeSet:
                return "" # Self Loop -> Requirement for topological sort is DAG 
            inDegree[y] = inDegree.get(y,0) + 1
            adjList[x].append(y)

        for char in allCharSet:
            if char not in inDegree:
                inDegree[char] = 0

        queue = []
        res = []

        for key in inDegree:
            if inDegree[key] == 0:
                queue.append(key)
        print(edgeSet)
        print(inDegree)
        while queue:
            newQueue = []

            for ele in queue:
                if ele not in adjList:
                    continue
                for nextEle in adjList[ele]:
                    inDegree[nextEle] -=1
                    if inDegree[nextEle] == 0:
                        newQueue.append(nextEle)
                     

            res = res + queue
            queue = newQueue[:]
        

        # Confirm if all inDegree have been resolved 
        if (sum(list(inDegree.values()))):
            # unresolved edges 
            return ""
        return "".join(res)

        

    
    def foreignDictionary(self, words: List[str]) -> str:
        # Constructing the graph
        edges = set()

        def identifyRelationship(str1, str2):

            n, m = len(str1), len(str2)
            minLen= min(n,m)

            for i in range(minLen):
                if str1[i] != str2[i]:
                    return (str1[i],str2[i])
            if minLen < m:
                if (str1[minLen-1]!=str2[minLen]):
                    return (str1[minLen-1],str2[minLen])
            return (0,0)

        allCharSet = set()

        n = len(words)

        for i in range(n):
            for j in range(i+1,n):
                relationship = identifyRelationship(words[i], words[j])

                if (relationship != (0,0)):
                    # valid relationship
                    edges.add(relationship)
                else:
                    if len(words[i]) > len(words[j]):
                        return ""
            allCharSet = allCharSet.union(set(list(words[i])))


        # returning the topological order 
        return self.topologicalOrdering(edges,allCharSet)
