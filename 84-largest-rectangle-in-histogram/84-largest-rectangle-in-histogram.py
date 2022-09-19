class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #bsaically we need the local minima on both sidde
        # so we need next smallest and previous smallest
        
        #we a need aincreasing stack
        stack = []
        n = len(heights)
        previousSmall = [-1]*(n)
        nextSmall = [n]*(n)

        for i in range(n):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                ele = stack.pop(-1)
                nextSmall[ele] = i
            
            stack.append(i)
            
        
        stack = []
        for i in range(n-1,-1,-1):
            
            while stack and heights[stack[-1]] >=heights[i]:
                ele = stack.pop(-1)
                previousSmall[ele] = i
            
            stack.append(i)
        
        maxArea = 0
        print(nextSmall)
        print(previousSmall)
        for i in range(n):
            width = nextSmall[i]-previousSmall[i]-1
            maxArea = max(width*heights[i],maxArea)
        
        return maxArea
            
            
            
        