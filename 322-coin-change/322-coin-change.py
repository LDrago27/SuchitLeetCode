class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        coins.sort()
        if amount == 0:
            return 0
        
        if coins[0]> amount:
            return -1
        
        dp = [0]*(amount+1)
        
        
        for amt in range(1,amount+1):
            temp = float('inf')
            for coin in coins:
                if coin > amt:
                    break
                temp = min(temp,1+dp[amt-coin])
            dp[amt] = temp
        
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]