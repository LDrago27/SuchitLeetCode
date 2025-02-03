class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Key insight: For continuos sub string kind of problems , more often than not one of the approaches that we should consider is sliding window
        # Advantages: Greedy may or not result in correct results depedning on the situation 
        # Dp requires more than 1 state considerations 

        charFreq = [0]*26 # since there are max 26 chars 

        start,end = 0,0
        n = len(s)

        def getIndex(charA):
            return ord(charA)-ord('A')

        res = 0
        while end<n:
            charFreq[getIndex(s[end])] +=1
            windowLength = end-start+1
            if windowLength-max(charFreq) > k:
                # Can't really convert them so we need to update the window
                charFreq[getIndex(s[start])] -=1
                start+=1
            res = max(res,end-start+1)
            end+=1
        
        return res

        