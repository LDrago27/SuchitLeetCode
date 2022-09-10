class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        n = len(height)
        end  = n-1
        area = 0
        
        while start<end:
            if height[start]> height[end]:
                area = max(area,(end-start)*height[end])
                end-=1
            else:
                area = max(area,(end-start)*height[start])
                start+=1
        return area