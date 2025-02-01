class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end = 0,0
        n = len(s)
        res = 0
        charMap = {}

        # Idea we slide a window whenever we get something that is ocverlappingh we move the start ot the index where it was firstr occuring

        while end < n:

            currChar = s[end]

            # This char has occured before
            while (currChar in charMap and charMap[currChar]!=-1) and start<=charMap[currChar]: 
                charMap[s[start]] = -1
                start +=1
            
            charMap[currChar] = end
            res = max(res,end-start+1)
            end+=1
        
        return res
