class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        maxAmt = 0
        
        start,end = 0,n-1
        
        while start<end:
            maxAmt = max(maxAmt,min(height[start],height[end])*(end-start))
            
            if height[start] > height[end]:
                end-=1
            else:
                start+=1
        
        return maxAmt
                
        