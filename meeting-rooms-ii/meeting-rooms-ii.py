class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTime,endTime = map(list,zip(*intervals))
        
        startTime.sort()
        endTime.sort()
        
        ctr = 0
        res = 0
        end = 0
        
        for start in startTime:
            if start < endTime[end]:
                ctr+=1
            else:
                end+=1
                ctr-=1
                ctr+=1
            res= max(res,ctr)
        
        return res