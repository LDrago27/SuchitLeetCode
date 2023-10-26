class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # State machine
        n = len(prices)
        
        # Lets say we have 2 states one where we have a stock on day[i] another wedon't have a stock on day[i]
        stockPres = [0]*n
        stockNotPres = [0]*n
        
        # when we sell we have to pay the price
        stockPres[0] = -prices[0]
        
        for i in range(1,n):
            p = prices[i]
            
            stockPres[i] = max(stockNotPres[i-1]-prices[i],stockPres[i-1]) # either bought it today or carried from prev
            stockNotPres[i] = max(stockPres[i-1]+prices[i]-fee,stockNotPres[i-1])# either sold it today or else carried forward from before 
            
        return stockNotPres[-1]
            