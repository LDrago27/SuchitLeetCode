class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        stack = []
        
        pairs.sort()
        res = 0
        for pair in pairs:
            
            if not stack or pair[0] > stack[-1][1]:
                stack.append(pair)
            else:
                if stack[-1][1] > pair[1]:
                    stack.pop()
                    stack.append(pair)
            
            res = max(res,len(stack))
        return res