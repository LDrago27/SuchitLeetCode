class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Divide and Conquer
        # We will divide the prices array into 2 halves
        # We will try to find atmost transaction in each halve
        
        # In first halve we need to find track the minValue and compute the profit with current element since it is of a form Buy and then Sell
        
        # In Second half we need to track the maxValue and compute profit with the current elment since it is of form Buy and Sell but we are moving in aopposite direction
        
        n = len(prices)
        leftSideProfit = [0]*n
        rightSideProfit = [0]*n
        
        minLeft = prices[0]
        maxRight = prices[-1]
        
        # Parition Point lies on the right side
        for i in range(n-2,-1,-1):
            maxRight = max(maxRight,prices[i])
            rightSideProfit[i] = max(rightSideProfit[i+1],maxRight-prices[i])
            
        for i in range(1,n):
            minLeft = min(minLeft,prices[i])
            leftSideProfit[i] = max(leftSideProfit[i-1],prices[i]-minLeft)
        
        res = 0
        for i in range(n):
            res = max(res,leftSideProfit[i]+rightSideProfit[i])
            
        return res
        
        
        
        