from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        
        start = 0
        end = 0
        n = len(s)
        tempCounter = {}
        res = float('inf')
        resStr = ""
        
        def checkValidCounter(c1,c2):
            
            for key in c2:
                if key in c1 and c1[key] >=c2[key]:
                    continue
                else:
                    return False
            
            return True
        
        while start<=end and end<n:
        
            while end<n and not checkValidCounter(tempCounter,tCounter):
                if s[end] in tCounter:
                    tempCounter[s[end]] = tempCounter.get(s[end],0)+1
                if checkValidCounter(tempCounter,tCounter):
                    break
                end+=1
            if checkValidCounter(tempCounter,tCounter) and res> end-start:
                resStr = s[start:end+1]
                res = min(res,end-start+1)
            #print(s[start:end])
            #print(start,end)
            while checkValidCounter(tempCounter,tCounter) and start<=end:
                if res> end-start:
                    resStr = s[start:end+1]
                    res = min(res,end-start+1)
                if s[start] in tCounter:
                    tempCounter[s[start]] = tempCounter.get(s[start])-1

                start+=1
            end+=1
            #print(s[start:end])

                
        return resStr