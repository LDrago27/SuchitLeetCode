class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        dp = [0] *(n+1)
        # dp indicates no of encoding from 0 to that index inclusive
        
        if s[0] == '0':
            return 0
        dp[0] = 1
        
        for i in range(1 ,n+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]# Consideering last didigt as one
            #Considering last two didigts
            
            if i>=2 and int(s[i-2:i])<=26 and s[i-2]!='0':
                dp[i] +=dp[i-2]
        
        return dp[n]
            
        