class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def generate(noLeft, noRight, currStr):
            
            if noLeft == noRight == n:
                res.append(currStr)
                return 
            if noLeft > n or noRight > n:
                return

            if noLeft < n:
                # We can add a left one
                generate(noLeft+1,noRight,currStr + "(")
                
            if noRight < noLeft:
                generate(noLeft,noRight+1,currStr + ")")
        
        generate(0,0,'')
        return res