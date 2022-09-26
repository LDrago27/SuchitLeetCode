class Solution:
    def calculate(self, s: str) -> int:
        # we will have something of a+b
        # if we get  + or - we append to a stack along with  operator however for * / we do it immediately
        
        stack = [0]
        curr = ''
        operator = '+'
        n = len(s)
        
        for i in range(n):
            if s[i] not in '+-*/':
                curr = curr+s[i]
            if s[i] in '+-*/' or i==n-1:
                if operator=='+':
                    stack.append(int(curr))
                elif operator=='-':
                    stack.append(-int(curr))
                elif operator=='*':
                    stack[-1]*=int(curr)
                else:
                    stack[-1]= int(stack[-1]/int(curr))
                
                curr = ''
                operator =s[i]
        return sum(stack)
            
            
            
        
        