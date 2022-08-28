from heapq import heapify,heappush,heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        # we need max number of overlaps happening
        
        heap = [[intervals[0][1],intervals[0][0]]]
        
        n = len(intervals)
        
        i = 1
        count = 1
        res = 0
        
        while i<n:
            
            nStart,nEnd = intervals[i]
            
            lastEnd = heap[0][0]
            lastStart = heap[0][1]
            res = max(res,count)
            
            if nStart< lastEnd:
                count+=1
                #print(lastStart,lastEnd)
            else:
                count-=1
                count+=1
                heappop(heap)
            heappush(heap,[nEnd,nStart])
            
            i+=1
        return max(res,count)
            
            
        