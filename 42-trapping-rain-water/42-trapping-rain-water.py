class Solution:
    def trap(self, height: List[int]) -> int:
        # at each position we can fill water till the height limit
        # height of water is the min of either boundary
        # we can make use of monotonic stack to get next great and prev greatest element
        n = len(height)
        maxleft = [0]*n
        maxright= [0]*n
        
        for i in range(1,n):
            maxleft[i] = max(maxleft[i-1],height[i-1])
        
        for i in range(n-2,-1,-1):
            maxright[i] = max(maxright[i+1],height[i+1])
            
        netarea  = 0
        
        #print(maxleft)
        #print(maxright)
        
        for i in range(n):
            waterlevel = min(maxleft[i],maxright[i])
            #print(height[i],waterlevel-height[i])
            if waterlevel-height[i]>=0:
                netarea+=waterlevel-height[i]
                
        return netarea