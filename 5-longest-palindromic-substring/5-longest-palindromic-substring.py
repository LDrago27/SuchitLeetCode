class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[False]*n for _ in range(n+1)]
        # n+1 rows each row is length while each col is starting index
        dp[0] = [True]*n
        dp[1] = [True]*n
        maxLen = 1
        maxStr = s[0]
        for l in range(2,n+1):
            for startIndex in range(0,n-l+1):
                if s[startIndex] == s[startIndex+l-1]:
                    dp[l][startIndex] = dp[l-2][startIndex+1]
                    if maxLen < l and dp[l][startIndex]:
                        maxLen = l
                        maxStr = s[startIndex:startIndex+l]
                    
        return maxStr
                    
                
        