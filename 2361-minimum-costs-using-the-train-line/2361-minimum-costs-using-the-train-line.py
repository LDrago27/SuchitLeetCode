class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        minCost = [[0]*(2) for _ in range(n+1)]
        minCost[0][1] = expressCost
        res= []
        # basically at each station there can be to ways he is at that given station came from eother regular or express way
        # 0 regular 1 express
        
        for i in range(n):
            # either he came from reg or from exp 
            #print(i)
            minCost[i+1][0] = min(minCost[i][0]+regular[i], minCost[i][1]+express[i])
            
            minCost[i+1][1] = min(minCost[i][0]+regular[i]+expressCost, minCost[i][1]+express[i])
        
            res.append(min(minCost[i+1][0],minCost[i+1][1]))
        return res
        

        