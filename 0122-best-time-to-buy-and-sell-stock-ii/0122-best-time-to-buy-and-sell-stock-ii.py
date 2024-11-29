class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''        Consider it is as a state machine so one where we always have the item and one where we don't .
        
        Case 1: We already have an item  -> prevProfit + choices either sell it or continue holding it 
        Case 2: We don't have an item. -> prevProfit -  choices either buy something or continue to not do anything
        
        Net will be max of both of the arrays i.e what comvbination gave the max Profit . 
        Exactloy the state transition does not matter as such. Since we don't get any adavantage for holding on to the same stock for days . So simply llop through the prices where we have oppurutnity to profit just do it 
    '''
    
        n = len(prices)
        profit = 0

        for i in range(1,n):
            if (prices[i] >= prices[i-1]):
                profit += prices[i] -prices[i-1]

        return profit 

    
    