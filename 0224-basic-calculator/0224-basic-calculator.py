class Solution:
    def calculate(self, s: str) -> int:
        listS = list(s.strip().split())
        s = ''.join(listS)
        operator = '+'
        prev = '0'
        curr ='0'
        stack = []
        for ele in s:
            #print(ele)
            if ele in '+-':
                # We need to evaluate the prev and set the current operator
                if operator == '+':
                    res = int(prev)+int(curr)
                else:
                    res = int(prev)-int(curr)
                    
                prev = str(res)
                operator = ele
                curr = '0'
            elif ele == '(':
                stack.append([prev,operator])
                operator = '+'
                prev = '0'
                curr = '0'
            elif ele==')':
                if operator == '+':
                    res = int(prev)+int(curr)
                else:
                    res = int(prev)-int(curr)
                
                stackTop, stackOp = stack.pop()
                
                if stackOp == '+':
                    res = res + int(stackTop)
                else:
                    res = int(stackTop) -res
                prev = str(res)
                operator = '+'
                curr = '0'
                
            else:
                curr = curr + ele
            #print(curr,prev,stack)
        if curr:
            if operator == '+':
                return int(prev)+ int(curr)
            else:
                return int(prev)-int(curr)
        else:
            return int(prev)
        
                
   
                    
