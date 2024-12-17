from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def computeMinCost(currDay):
            if currDay<=0:
                return float('inf')
            
            if currDay in cache:
                return cache[currDay]
            
            lim1, lim2, lim3 = currDay-1 +1 , currDay-7+1, currDay-30+1
            
            res = float('inf')
            
            bisect1 = bisect_left(days, lim1)
            if bisect1 == 0:
                res = min(res,costs[0])
            else:
                res= min(res,costs[0]+computeMinCost(days[bisect1-1]))
                
            bisect2 = bisect_left(days, lim2)
            
            if bisect2 == 0:
                res = min(res,costs[1])
            else:
                res= min(res,costs[1]+computeMinCost(days[bisect2-1]))
                
              
            bisect3 = bisect_left(days, lim3)
            
            if bisect3 == 0:
                res = min(res,costs[2])
            else:
                res= min(res,costs[2]+computeMinCost(days[bisect3-1]))
            
            cache[currDay] = res
            return cache[currDay]
        
        
        return computeMinCost(days[-1])