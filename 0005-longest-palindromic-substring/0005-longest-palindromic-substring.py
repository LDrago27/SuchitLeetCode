class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Idea 2: Expanding from centers
        
        n = len(s)
        
        def expand(left,right):
            if left < 0 and right >=n:
                return n
            elif left <0:
                return right - left -1
            elif right>=n:
                return right - left -1
            
            if s[left]==s[right]:
                return expand(left-1,right+1)
            else:
                return right-left-1
            
        res = 0
        resStr = ""
        for i in range(n):
            oddLen = expand(i,i)
            evenLen = expand(i,i+1)
            if res < oddLen:
                res = oddLen
                resStr = s[i-oddLen//2:i]+s[i]+s[i+1:i+oddLen//2+1]
            if res < evenLen:
                res= evenLen
                rem = (evenLen - 2) // 2
                resStr = s[i-rem:i]+s[i:i+2]+s[i+2:i+rem+2]
                
        return resStr