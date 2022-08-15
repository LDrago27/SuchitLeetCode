class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        # similar to prev question we have now k buys and k sell and each is dependent on prior
        # buy reduces the current money
        # sell increases the money
        # one caveat is value of k if the value of k is greater than n//2 it is equivalent to making infinte no of trancastion
        n = len(prices)
        if k==0:
            return 0
        
        if k> n//2:
            # now we have infinter number of tries
            profit = 0
            for i in range(n-1):
                if prices[i+1]>prices[i]:
                    profit += prices[i+1]-prices[i]
            return profit
        else:
            sell = [float('-inf')]*k
            buy = [float('-inf')]*k
            
            for i in range(n):
                
                for j in range(k):
                    if j == 0:
                        buy[j] = max(buy[j],-prices[i])
                    else:
                        buy[j] = max(sell[j-1]-prices[i],buy[j])
                        
                    sell[j] = max(buy[j]+prices[i],sell[j])
            #print(sell)
            return sell[-1]
                        
                        
            
        
                        
                        
            
            
        