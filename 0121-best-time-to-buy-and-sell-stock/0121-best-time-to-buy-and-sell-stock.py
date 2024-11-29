class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceTillNow = float('inf')
        
        maxProfit = 0
        
        for price in prices:
            minPriceTillNow = min(price, minPriceTillNow)
            maxProfit = max(maxProfit, price - minPriceTillNow)
        
        return maxProfit 