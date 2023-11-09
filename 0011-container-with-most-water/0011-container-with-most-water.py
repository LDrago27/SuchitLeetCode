class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left , right = 0, n-1
        
        res = 0
        while left < right:
            
            if height[left] < height[right]:
                res = max(res, height[left]*(right-left))
                left += 1
            else:
                res = max(res, height[right]*(right-left))
                right -= 1
        return res
                