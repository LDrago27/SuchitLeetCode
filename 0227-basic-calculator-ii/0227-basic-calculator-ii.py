class Solution:
    def calculate(self, s: str) -> int:
        listS = list(s.strip().split())        
        s = ''.join(listS)
        s = s+'+'
        stack = []
        prev = '+'
        curr = '0'
        for ele in s:
            
            if ele in '+-*/':
                if prev in '*/':
                    
                    if prev == '*':
                        stack.append(stack.pop()*int(curr))
                    else:
                        prevEle = stack.pop()
                        sign = 1 if prevEle >= 0 else -1 
                        stack.append((abs(prevEle)//int(curr))*sign)
                    
                else:
                    
                    if prev == '+':
                        stack.append(int(curr))
                    else:
                        stack.append(int(curr)*-1)
                    
                prev = ele
                curr = '0'
            else:
                curr = curr + ele
        
        
        return sum(stack)
        
        