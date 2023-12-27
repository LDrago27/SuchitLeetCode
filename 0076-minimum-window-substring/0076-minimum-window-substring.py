from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # idea first expand it till we get a match and then contract it
        counterT = Counter(t)
        n = len(s)
        counterTemp = {}
        
        def isValid(counterTemp,counterT):
            
            for key in counterT:
                if key not in counterTemp:
                    return False
                if counterT[key] > counterTemp[key]:
                    return False
                
            return True
        
        start = 0
        res, resStr = float('inf'), ""
        for i in range(n):
            counterTemp[s[i]] = counterTemp.get(s[i],0)+1
                            
            # Trying out compression
            while start<=i and isValid(counterTemp,counterT):
                if res > i-start+1:
                    res = i-start+1
                    resStr = s[start:i+1]
                counterTemp[s[start]]-=1
                start+=1
                
                
        return resStr
