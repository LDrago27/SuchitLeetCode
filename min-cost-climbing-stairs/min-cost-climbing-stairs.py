class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        minCost = [0]*(n+1)
        
        for i in range(2,n+1):
            minCost[i] = min(minCost[i-2]+cost[i-2],minCost[i-1]+cost[i-1])
        
        return minCost[-1]