class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # We can use a dp of sorts
        n,m = len(s), len(p)
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[0][0] = True # basically when both the pattern and string is empty
        
        for i in range(m):
            if p[i] == '*':
                dp[i+1][0] = dp[i-1][0]
                

        # base conditions are ready now we can start filling it up
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if p[i-1] == '*':
                    dp[i][j] = dp[i-2][j] #0 matches of prev character
                    
                    if p[i-2] == '.' or p[i-2] == s[j-1]:
                        dp[i][j] = dp[i][j] or dp[i][j-1]
                    
                elif p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1] # mathcing the last character
                    
                elif p[i-1]==s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
        return dp[-1][-1]
                
                
        
        