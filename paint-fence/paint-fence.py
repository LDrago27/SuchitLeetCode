class Solution:
    def numWays(self, n: int, k: int) -> int:
        # we will sub divide the problem into parts
        # last two colors same and last two colors different
        # 0 -> same, 1-> different
        dp = [[0,0]for _ in range(n+1)]
        
        if n==1:
            return k
        
        else:
            # last two colors are same
            #print(len(dp))
            dp[2][0] = k*1
            # last two colors are diffrent
            dp[2][1] = k *(k-1)
            
            for i in range(3,n+1):
                
                # last two colors are same we can take last 2 color diff of prev and just use same color as that of last we can't do the same for two same since it would result in 3 consequtive colors being same
                dp[i][0] = dp[i-1][1]
                # we take all combo and jus take a color diif than last selected one
                dp[i][1] = (dp[i-1][1]+dp[i-1][0])*(k-1)
                
            return sum(dp[-1])
                
                
        
        
        