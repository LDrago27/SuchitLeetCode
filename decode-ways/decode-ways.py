class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        if s[0] == '0':
            return 0
        dp[1] = 1
        dp[0] = 1
        for i in range(1,n):
            choice1 = s[i]
            choice2 = s[i-1:i+1]
            print(choice1,choice2)
            if choice2[0] !='0' and int(choice2) in range(1,27):
                dp[i+1] += dp[i-1]
            if choice1!='0':
                dp[i+1]+= dp[i]
        
        print(dp)
    
        return dp[-1]
