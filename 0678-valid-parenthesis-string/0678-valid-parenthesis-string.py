class Solution:
    def checkValidString(self, s: str) -> bool:
        # We need to reset the ctr of star till the stack is empty
        stack = []
        star = []
        for index,ele in enumerate(s):
            
            if ele == '(':
                stack.append([index,ele])
            elif ele == '*':
                star.append([index,ele])
            else:
                if stack:
                    stack.pop()
                else:
                    if star:
                        star.pop()
                    else:
                        return False
        while stack:
            index,ele = stack.pop()
            if not star:
                return False
            if star[-1][0] < index:
                # start is before this opening bracket henc it is invalid
                return False
            star.pop()

        return True
                    
                