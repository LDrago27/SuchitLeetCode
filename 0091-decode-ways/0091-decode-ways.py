class Solution:
    def numDecodings(self, s: str) -> int:
        
        # At each index we have two choice either include current element or include both this and next element
        
        n = len(s)
        dp = [0]*(n+1)
        
        dp[0],dp[1] = 1, 1
        
        if s[0]=='0':
            return 0
        
        for i in range(1,n):
            
            if s[i] != "0":
                dp[i+1] = dp[i]
            
            if s[i-1]!='0' and int(s[i-1:i+1]) <=26:
                dp[i+1] += dp[i-1]
        
        return dp[-1]
        