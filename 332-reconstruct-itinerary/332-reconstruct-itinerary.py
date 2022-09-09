from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key = lambda x: x[0]+x[1])
        
        # we have sorted the array to handle lexxical case
        # now we use JFk as start and continue moving tioioll all edges are done
        
        graph = defaultdict(list)
        netEdgeCount = {}
        currEdgeCount = {}
        
        # we need to have a visited edge array
        for x,y in tickets:
            graph[x].append(y)
            netEdgeCount[(x,y)] = netEdgeCount.get((x,y),0)+1
            currEdgeCount[(x,y)] = 0
        #print(netEdgeCount)
        n = len(tickets)
        res = []
        
        def util(currNode,pathTillNow,currEdgeCount):
            #print(currNode,pathTillNow,currEdgeCount)
            if len(pathTillNow) == n:
                res.append(pathTillNow+[currNode])
                return True
            
            for neighbour in graph[currNode]:
                if currEdgeCount[(currNode,neighbour)]!=netEdgeCount[(currNode,neighbour)]:
                    currEdgeCount[(currNode,neighbour)] += 1
                    
                    if util(neighbour,pathTillNow+[currNode],currEdgeCount):
                        return True
                    
                    currEdgeCount[(currNode,neighbour)]-=1
            return False
        
        util('JFK',[],currEdgeCount)
        return res[0]
            