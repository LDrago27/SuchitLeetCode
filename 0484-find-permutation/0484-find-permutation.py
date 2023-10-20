class Solution:
    def findPermutation(self, s: str) -> List[int]:
        
        n = len(s)
        res = []
        for i in range(1,n+2):
            if not res:
                res.append(i)
                
            else:
                
                if s[i-2] == 'I':
                    res.append(i)
                else:
                    
                    
                    newStack = []
                    temp =i-2
                    while s[temp]=='D' and temp >=0:
                        newStack.append(res.pop())
                        temp-=1
                        
                    res.append(i)
                    while newStack:
                        res.append(newStack.pop())
                    
                    #print(i,res)  
        return res