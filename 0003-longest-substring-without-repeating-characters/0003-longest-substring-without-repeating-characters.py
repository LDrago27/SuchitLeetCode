class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Idea: create a hashmap that stores the index of occurence of element
        # if that element occurs again then shift start to the index+1
        # remove elements between prev start and current index+1
        
        res = 0
        start = 0
        n = len(s)
        indexOccur = {}
        for i in range(n):
            ele = s[i]
            
            if ele not in indexOccur:
                indexOccur[ele] = i
            else:
                # prev Occurance +1
                newStart = indexOccur[ele] +1
                
                # remove stuff between start and newStart
                
                for j in range(start,newStart):
                    indexOccur.pop(s[j])
                
                indexOccur[ele] = i
                start = newStart
            res = max(res,i-start+1)
        
        return res