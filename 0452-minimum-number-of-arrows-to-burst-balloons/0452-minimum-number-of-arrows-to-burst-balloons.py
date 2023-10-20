class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Idea is find the intersection areas put one there 
        # For disconnected just add them up
        
        points.sort()
        
        start,end = points[0]
        overlap = []
        count = 0
        n = len(points)
        for i in range(1,n):
            # prev Overlap is present
            if overlap:
                # Do we have a overlap with prev
                if points[i][0] <= overlap[0][1]:
                    overlap[0][1] = min(overlap[0][1],points[i][1])
                    
                else:
                    #New one
                    count +=1 # count prev one
                    overlap = []
                    start,end = points[i]
            else:
                
                if points[i][0]<=end:
                    overlap.append([points[i][0],min(points[i][1],end)])
                    
                else:
                    count +=1
                    start,end = points[i]
                
        
        count +=1
            
        return count