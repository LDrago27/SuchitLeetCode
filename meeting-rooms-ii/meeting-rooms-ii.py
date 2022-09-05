class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        startTimes,endTimes = map(list,zip(*intervals))
        
        n = len(intervals)
        
        startTimes.sort()
        endTimes.sort()
        
        end = 0
        room = 0
        res = 0
        
        for i in range(n):
            
            if startTimes[i] < endTimes[end]:
                room+=1
            else:
                end+=1
                room-=1
                room+=1
            res = max(res,room)
        return res