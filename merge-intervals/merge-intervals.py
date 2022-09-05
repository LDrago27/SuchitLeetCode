class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        n = len(intervals)
        res = []
        
        currStartTime,currEndTime = intervals[0]
        
        i = 1
        while i<n:
            
            if intervals[i][0] <= currEndTime:
                currEndTime = max(currEndTime,intervals[i][1])
            else:
                res.append([currStartTime,currEndTime])
                currStartTime,currEndTime = intervals[i]
            
            i+=1
        
        res.append([currStartTime,currEndTime])
        
        return res
                
                