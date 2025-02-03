class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False

                topEle = stack.pop()
                if (topEle == '(' and char !=')') or (topEle == '{' and char !='}') or (topEle == '[' and char !=']'):
                    return False
        return True if not stack else False
        