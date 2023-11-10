class Solution:
    def longestValidParentheses(self, s: str) -> int:
        

        # Idea is tha t we will store both the open and close bvracketws with index in the stack and use that to compute length
        
        stack = [['#',-1]]
        res = 0
        for index,ele in enumerate(s):
            
            if ele == '(':
                stack.append([ele,index])
                
            else:
                
                if stack[-1][0] == '(':
                    stack.pop()
                    res = max(res,index-stack[-1][1])
                else:
                    stack.append([ele,index])
        return res