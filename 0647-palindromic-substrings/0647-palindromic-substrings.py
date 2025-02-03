class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False]*n for _ in range(n)]
        res = 0

        for i in range(n):
            dp[i][i] = True
            res +=1
        
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                res +=1
        
        for length in range(3,n+1):
            for start in range(n-length+1):
                if s[start] == s[start+length-1]:
                    if dp[start+1][start+length-2]:
                        dp[start][start+length-1] = True
                        res +=1        
        return res