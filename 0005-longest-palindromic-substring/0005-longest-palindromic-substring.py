class Solution:
    def longestPalindrome(self, s: str) -> str:
        # classic Dp problem 
        # Iterate by length and not anything else
        n = len(s)

        dp = [[False]*n for _ in range(n)]
        res,resStr = 0, ""

        for i in range(n):
            dp[i][i] = True
            resStr = s[i]
        
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                resStr = s[i:i+2]
        
        for length in range(3,n+1):
            for start in range(n-length+1):
                if s[start] == s[start+length-1]:
                    if dp[start+1][start+length-2]:
                        dp[start][start+length-1] = True
                        resStr = s[start:start+length]
        
        return resStr

        