class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buyPrice = prices[0]
        res = 0
        
        for i in range(1,n):
            if buyPrice > prices[i]:
                buyPrice = prices[i]
            else:
                res = max(res,prices[i]-buyPrice)
        return res