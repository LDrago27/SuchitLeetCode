from heapq import heapify,heappop,heappush
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # we can use bucket sort O(N) + O(S)
        
        res = 0
        heapify(sticks)
        res = 0
        while len(sticks)>1:
            ele1 = heappop(sticks)
            ele2 = heappop(sticks)
            res+=ele1+ele2
            heappush(sticks,ele1+ele2)
        
        return res
        