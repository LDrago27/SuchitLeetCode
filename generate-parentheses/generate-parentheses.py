class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # so we ill have max n open nadd n close bracket
        res = []
        
        def recurr(noOpen,noClose,currArr):
            
            if noOpen == noClose == n:
                res.append(''.join(currArr))
                return
            
            if noOpen <n:
                recurr(noOpen+1,noClose,currArr+['('])
            
            if noClose<noOpen:
                recurr(noOpen,noClose+1,currArr+[')'])
                
        recurr(0,0,[])
        return res
            
            