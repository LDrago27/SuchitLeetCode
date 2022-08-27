class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        n = len(height)
        
        end = n-1
        resArea = 0
        
        while start<end:
            resArea = max(resArea, (end-start)*min(height[end],height[start]))
            #print(start,end,resArea)
            
            if height[end]> height[start]:
                start+=1
            else:
                end-=1
        
        return resArea
            