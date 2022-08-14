class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text2)
        m = len(text1)
        dp = []
        
        for _ in range(m):
            dp.append([0]*n)
            
        if text1[0]==text2[0]:
            dp[0][0]=1
            
        for i in range(m):
            if text1[i] == text2[0]:
                dp[i][0] =1
            else:
                dp[i][0] = dp[i-1][0]
                
        for j in range(n):
            if text1[0] == text2[j]:
                dp[0][j]=1
            else:
                dp[0][j] = dp[0][j-1]

                
        for i in range(1,m):
            for j in range(1,n):
                
                if text2[j] == text1[i]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        #print(dp)
        return dp[-1][-1]