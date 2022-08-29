class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
       # For a O(n) solution take an element how many cases will that number be max or min 
       # so basically for each number wwe need two values .e prev greater and nextgreater
        # same thing for min values
        
        n = len(nums)
        
        prevLess = [-1]*n
        nextLess = [n]*n
        prevGreat = [-1]*n
        nextGreat = [n]*n
        
        ngStack = [] # decreasing
        pgStack = [] # decreasing
        plStack = [] # increasing
        nlStack = [] # increasing
        
        
        for i in range(n):
            
            while ngStack and nums[ngStack[-1]]<nums[i]:
                index  = ngStack.pop()
                nextGreat[index] = i
            
            ngStack.append(i)
            
            while pgStack and nums[pgStack[-1]]<=nums[n-1-i]:
                index = pgStack.pop()
                prevGreat[index] = n-1-i
            
            pgStack.append(n-1-i)
            
            while nlStack and nums[nlStack[-1]] > nums[i]:
                index = nlStack.pop()
                nextLess[index] = i
            
            nlStack.append(i)
            
            while plStack and nums[plStack[-1]] >= nums[n-1-i]:
                index = plStack.pop()
                prevLess[index] = n-1-i
            
            plStack.append(n-1-i)
        maxVal, minVal = 0,0
        for i in range(n):
            maxVal  += (i-prevGreat[i])*(nextGreat[i]-i)*nums[i]
            minVal += (i-prevLess[i])*(nextLess[i]-i)*nums[i]
        
        #print(prevGreat)
        #print(nextGreat)
        #print(prevLess)
        #print(nextLess)
        
        return maxVal -minVal
            
            
        
        