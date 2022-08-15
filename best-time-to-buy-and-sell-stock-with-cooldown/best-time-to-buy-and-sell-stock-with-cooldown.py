class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        cache = {}
        
        
        def profitUtil(i,state):
            if i>=n:
                return 0
            if (i,state) not in cache:
    
                if state == 1:
                    # basically we have to sell or keep that
                    res = max(profitUtil(i+1,state),prices[i]+profitUtil(i+2,0))
                else:
                    res = max(profitUtil(i+1,state),profitUtil(i+1,1)-prices[i])
                
                cache[(i,state)] = res
            return cache[(i,state)]
            
        return profitUtil(0,0)