class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        positive = 1
        n = len(s)
        i = 0
        
        if n==0:
            return 0

        if s[0] == '-':
            positive = -1
            i+=1
        elif s[0]=='+':
            i+=1
        
        # reach the non zero diigt
        
        while i<n and s[i]=='0':
            i+=1     
        # reached the non zero char now we can start the string
        res = 0
        print(positive)
        while i<n and s[i] in '0123456789':
            res = res*10+int(s[i])
            print(res)
            if res >= (2**31-1) and positive == 1:
                return 2**31-1
            if res >= 2**31 and positive == -1:
                return -2**31
            i+=1
        return res*positive
            