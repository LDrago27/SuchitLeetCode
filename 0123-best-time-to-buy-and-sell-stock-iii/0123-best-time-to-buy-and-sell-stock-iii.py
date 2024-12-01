class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Great Question 
        # Idea is Divide and Conquer 
        # At any given point i the left side and right side the given point i for example can be considered as the divison point and we need one trasaction on either side of point i 
        
        leftSideMin = prices[0]
        rightSideMax = prices[-1]
        
        n = len(prices)
        
        leftProfit = [0]*n
        rightProfit = [0]*n
        
        # Populating the leftProfit 
        # Skipping 0 since it is not included in the left Side At all 
        
        for i in range(1,n):
            leftSideMin = min(leftSideMin, prices[i-1])
            leftProfit[i] = max(leftProfit[i-1],prices[i-1]-leftSideMin) # That is we either do nothing or sell at i-1
            
        # Populating rightProfit
        # We need to move in a reverse fashion and here we are assuming thatn we are seelign at given price
        for i in range(n-2,-1,-1):
            rightSideMax = max(rightSideMax, prices[i])
            rightProfit[i] = max(rightProfit[i+1], rightSideMax-prices[i])
            
        
        # Net Profit is max 
        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, leftProfit[i]+rightProfit[i])
            
        return maxProfit 