class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        coins.sort()
        start = coins[0]
        for amt in range(start,amount+1):
            tempRes = float('inf')
            for coin in coins:
                if coin<=amt:
                    tempRes = min(tempRes,1+dp[amt-coin])
                else:
                    break
            dp[amt] = tempRes
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]
                
            