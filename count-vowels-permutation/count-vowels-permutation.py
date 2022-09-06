class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        # so we need to not only keep track of n length but also the last character entered
        # since we have a,e,i,o,u we will create a adp accordingly
        # row number is length and cloumn correspond to aeiou
        
        dp = [[0]*5 for _ in range(n+1)]
        dp[1] = [1]*5
        base = 10**9 + 7
        for i in range(2,n+1):
            

            # ending in a so it can from e,i,u
            dp[i][0] = (dp[i-1][1]+ dp[i-1][2] + dp[i-1][4])
            
            # ending in e so it can from a,i
            dp[i][1] = dp[i-1][0]+ dp[i-1][2]
            
            # ending in i so it can from e,o
            dp[i][2] = dp[i-1][1] + dp[i-1][3]
            
            #ending in o so it can from i
            dp[i][3] = dp[i-1][2]
            
            #ending in u so it can from i,o
            dp[i][4] = dp[i-1][2] + dp[i-1][3]
            
        return sum(dp[-1])%(base)