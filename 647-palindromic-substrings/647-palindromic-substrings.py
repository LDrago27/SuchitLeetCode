class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        dp = [[False]*n for _ in range(n)]
        
        # palindrome of len 1
        for i in range(n):
            dp[i][i] = True
        
        # plaindrome of len 2
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
        
        for palinLen in range(3,n+1):
            for i in range(n-palinLen+1):
                if s[i] == s[i+palinLen-1]:
                    dp[i][i+palinLen-1] = dp[i+1][i+palinLen-2]
        res =0
        for i in range(n):
            for j in range(i,n):
                if dp[i][j]:
                    res+=1
        
        return res
        