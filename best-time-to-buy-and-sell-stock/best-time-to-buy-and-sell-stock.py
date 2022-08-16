class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = float('inf')
        n = len(prices)
        for i in range(n):
            if prices[i]<buy:
                buy = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i]-buy)
        return maxProfit
            