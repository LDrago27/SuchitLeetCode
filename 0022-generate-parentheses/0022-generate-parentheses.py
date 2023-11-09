class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def buildString(left,right,currStr):
            
            
            if right == n and left == n:
                res.append(currStr)
                return
            
            if left > n or right >n:
                return
            
            if left > right:
                # We have two options we can put a left bracket or a right bracket
                # Case 1 : left bracket
                buildString(left+1,right,currStr+'(')
                # Case 2 : right bracket
                buildString(left,right+1,currStr+')')
            elif left == right:
                buildString(left+1,right,currStr+'(')
                # We can add only left bracket
            return
        buildString(1,0,'(')
        return res
                
                
            
            
        