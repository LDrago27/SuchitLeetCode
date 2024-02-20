from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # Idea is that at any given start time we need to evivt people whose meeting times have ended before that how to get that minHeap of endTimes
        
        intervals.sort(key = lambda x:(x[0],x[1])) # O(nlogn)
        
        rooms = [] # minHeap of endTimes
        res = 0
        for start,end in intervals:
            
            while rooms and rooms[0] <= start:
                heappop(rooms)
            
            heappush(rooms,end)
            res = max(res,len(rooms))
            
        return res
        
        