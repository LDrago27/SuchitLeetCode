class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        
        dp = [0]*(amount+1)
        dp[0] = 1
        
        # here dp should ideally be a 2d dp with amount and individual coin indices
        # If we use only last amt to calculate current value there are repetititon for eg to make 5 using 1,2,3 if we use amt method we need to 1 + dp(4) or 2+dp(3) here 1,2,2 1,2,2 will be repeated
        # so we need to use the coins i.e we fill in using coins indices and then do it
        
        for coin in coins:
            for amt in range(coin,amount+1):
                #print(amt,coin)
                dp[amt] += dp[amt-coin]
        
        return dp[-1]
        