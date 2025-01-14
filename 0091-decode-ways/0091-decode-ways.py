class Solution:
    def numDecodings(self, s: str) -> int:
        decodeDict = {}

        for i in range(1,26):
            decodeDict[str(i)] = chr(ord("A") + (i-1))
        
        res = 0
        n = len(s)
        dp = [0]*n

        if s[0] != '0':
            dp[0] = 1

        for i in range(1,n):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2] if i-2 >= 0 else 1
        
        return dp[-1]
            
