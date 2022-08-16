class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        buy = float('-inf')
        sell = 0
        
        for ele in prices:
            buy = max(buy,sell-ele)
            sell = max(sell, buy+ele-fee)
            
        return sell