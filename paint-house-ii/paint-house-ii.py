from heapq import heapify,heappop
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m = len(costs)
        n = len(costs[0])
        dp = [[0]*n for _ in range(m) ]
        dp[0] = costs[0]
        #heap = [(dp[0][i],i) for i in range(n)]
        #heappify(heap)
        
        for i in range(1,m):
            for color in range(n):
                temp = float('inf')
                
                for k in range(n):
                    if k==color:
                        continue
                    temp = min(temp,dp[i-1][k])
                dp[i][color] = costs[i][color]+temp
        
        return min([dp[-1][i] for i in range(n)])
        
        