class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        lookup= {}
        tempLen = 0
        res = 0
        start = 0
        
        for i in range(n):
            if s[i] not in lookup or lookup[s[i]]==-1:
                lookup[s[i]] = i
                tempLen+=1
                res = max(res,tempLen)
            else:
                end = lookup[s[i]]
                
                while start<=end and end <n:
                    lookup[s[start]] = -1
                    tempLen-=1
                    start+=1
                lookup[s[i]] =i
                tempLen += 1
        #print(lookup)
        return res
                
                
            