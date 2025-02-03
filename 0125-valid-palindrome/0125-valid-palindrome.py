class Solution:
    def isPalindrome(self, s: str) -> bool:

        def processString(s):
            res = []

            for char in s:
                if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                    res.append(char.lower()) 
                elif char in '0123456789':
                    res.append(char) 

            return ''.join(res)

        processedS = processString(s)
       #print(processedS)
        n = len(processedS)


        for i in range(n):
            if processedS[i] != processedS[n-i-1]:
                return False
        
        return True

        