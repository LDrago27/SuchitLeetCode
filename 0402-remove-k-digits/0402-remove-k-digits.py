class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # Idea is to keep track of the peaks and try to convert it into ascending order as much as possible
        
        stack = []
        n = len(num)
        i = 0
        while i<n:
            if k==0:
                break
            ele = num[i]
            if not stack:
                if ele != '0':
                    stack.append(ele)
            else:

                while stack and stack[-1] > ele and k:
                    k-=1
                    stack.pop()
                    
                if not (not stack and ele == '0'):
                    stack.append(ele)
            i+=1
        while i<n:
            if not stack and num[i] == '0':
                i+=1
            else:
                stack.append(num[i])
                i+=1
        while stack and k!=0:
            k-=1
            stack.pop()

        
        netRes = ''.join(stack)
        
        if not netRes:
            return '0'
        return netRes
        
        