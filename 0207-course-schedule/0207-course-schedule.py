from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        outDegree = {}
        for i in range(numCourses):
            outDegree[i]=0

        graph = defaultdict(list)

        for a,b in prerequisites:
            outDegree[a] +=1
            graph[b].append(a) # Storing the edge in a inverted manner for ease of accesss

        queue = []

        for i in range(numCourses):
            if outDegree[i] == 0:
                queue.append(i)

        while queue:
            newQueue = []

            for ele in queue:

                for prevEle in graph[ele]:
                    outDegree[prevEle] -=1
                    if outDegree[prevEle] == 0:
                        newQueue.append(prevEle)
            queue = newQueue[:]

        return sum(list(outDegree.values())) == 0





        
