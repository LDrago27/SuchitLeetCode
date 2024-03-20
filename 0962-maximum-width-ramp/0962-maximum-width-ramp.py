from bisect import bisect_right
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        # Idea is to storte the numbers in a descending order 
        # Imagine we have 0, then we have 8 should we store 8 no since if a number satisfies for 8 it inherently does so for 0 so no need to store for 8 
        
        stack = []
        
        maxWidth = 0
        
        n = len(nums)
        
        
        for i in range(n):
            
            # Find the positon where we have the max
            # Linear search now from start can be upgraded to a binary search
            m = len(stack)
            if stack:

                invertedIndex = m - bisect_right(stack[::-1],(nums[i],n))

                if invertedIndex<m and stack[invertedIndex][0] <= nums[i]:
                    maxWidth = max(maxWidth, i-stack[invertedIndex][1])
                
                #print(invertedIndex, stack, nums[i], maxWidth)

            if stack and stack[-1][0] < nums[i]:    
                continue
            else:
                stack.append((nums[i],i))
                
        
        return maxWidth
        