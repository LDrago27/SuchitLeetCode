class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Idea is the dp willl be on the net amount 
        # Since the sub problems can be converted based on amounts so at ever point it is the amount and how many ways can it be made 
        
        dp = [float('inf')]*(amount+1)
        
        dp[0]=0
        
        coins.sort()
        
        for amt in range(1,amount+1):
            tempRes = float(inf)
            for coin in coins:
                if amt < coin:
                    break
                tempRes = min(tempRes,1+dp[amt-coin])
            dp[amt] = tempRes
        #print(dp)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
    
                
        