class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        # So basically we are going evaluate all 4^ (n-1) possiblity to find the result
        
        n = len(num)
        res = []
        
        def checkZeroPrefix(str1):
            i = len(str1)-1
            while i>=0 and str1[i]=='0':
                i-=1
            
            if i==-1:
                return True
            elif str1[i] in '+-*':
                return True
            else:
                return False
                
            
            
        
        def recurr(index,expression):
            #print(index,expression)
            if index == n-1:
                if calculate(expression+num[index]) == target:
                    res.append(expression+num[index])
                return 
            
            
            # Option 1 Insert + after index
            recurr(index+1,expression+num[index]+'+')
    
            # Option 2 Insert - after index 
            recurr(index+1,expression+num[index]+'-')
            
            #Option 3 Insert * after index
            recurr(index+1,expression+num[index]+'*')

            #Option 4 DO nothing
            if num[index]!='0' or not checkZeroPrefix(expression+num[index]):            
                recurr(index+1,expression+num[index])

        
        
        
        def calculate(s: str) -> int:
            # Evaluate an expression.
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
        
        recurr(0,'')
        return res