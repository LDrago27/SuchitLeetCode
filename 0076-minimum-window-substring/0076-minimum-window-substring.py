from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        counterT = Counter(t)


        def isValidSubString(currStrCounter):

            for key in counterT:
                if key not in currStrCounter or currStrCounter[key] < counterT[key]:
                    return False
            return True

        
        start,end = 0,0
        currStrCounter = {}
        res = float('inf')
        resStr = ""

        n = len(s)
        while end<n:
            currStrCounter[s[end]] = currStrCounter.get(s[end],0) + 1 # Updating the counter

            while start<=end and isValidSubString(currStrCounter):
                if end-start+1 <= res:
                    res = end-start+1
                    resStr = s[start:end+1]
                # try to reduce squeeze
                currStrCounter[s[start]] -=1 
                start +=1
            
            end+=1
        return resStr
        
        