class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        prefixSum = [0]*(n+1)
        prefixSum[0] = 0
        
        netPrefixSum = [0]*(n+2)
        for i in range(1,n+1):
            prefixSum[i] = prefixSum[i-1]+strength[i-1]
        
        netPrefixSum[0] = 0
        for i in range(1,n+2):
            netPrefixSum[i] = prefixSum[i-1]+netPrefixSum[i-1]
            
        previousSmall = [-1]*(n)
        nextSmall = [n]*(n)
        
        # we will use increasing monontic stack for this
        stack = []
        for i in range(n):
            
            while stack and strength[stack[-1]] > strength[i]:
                index = stack.pop()
                nextSmall[index] = i
            
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            
            while stack and strength[stack[-1]] >= strength[i]:
                index = stack.pop()
                previousSmall[index] = i
                
            stack.append(i)
        res = 0
        #print(nextSmall)
        #print(previousSmall)
        #print(prefixSum)
        #print(netPrefixSum)
        for i in range(n):
            lb = previousSmall[i]
            ub = nextSmall[i]
            noEleLeft = i-lb
            noEleRight = ub-i
            temp = 0
            #print(strength[i])
            #print(lb,ub)
            #print(noEleRight,noEleLeft)
            # so each of the right half prefix can be user 
            temp += noEleLeft*(netPrefixSum[ub+1]-netPrefixSum[i+1])
            temp-= noEleRight*(netPrefixSum[i+1]-netPrefixSum[lb+1])
            res += temp*strength[i]
            #print("Yo",temp)
        return res%(10**9+7)
            
        
        