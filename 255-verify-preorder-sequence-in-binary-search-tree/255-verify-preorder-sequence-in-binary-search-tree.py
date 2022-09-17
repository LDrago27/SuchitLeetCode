class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        prevElement = float('-inf')
        stack = []
        n = len(preorder)
        
        for i in range(n):
            
            if preorder[i]< prevElement:
                return False
            
            while stack and stack[-1] < preorder[i]:
                prevElement = stack.pop()
            
            stack.append(preorder[i])
        
        return True