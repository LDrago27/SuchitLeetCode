from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:(x[0],x[1]))
        
        curr = 0
        res = 0
        
        heap = [] # on the basis of the endTime minHeap

 

        for start,end in intervals:
            # Free up stuff min Edn time less than start time we remove
            while heap and heap[0][0] <= start:
                heappop(heap)
                curr-=1
                
            heappush(heap,[end,start])
            curr+=1
            
            res = max(res,curr)
            
        return res