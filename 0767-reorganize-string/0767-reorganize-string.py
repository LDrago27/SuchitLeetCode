from collections import Counter
from heapq import heappop,heappush,heapify
class Solution:
    def reorganizeString(self, s: str) -> str:
        used = []
        maxHeap = []
        
        ctr = Counter(s)
        
        for key in ctr:
            maxHeap.append([ctr[key]*-1,key])
        heapify(maxHeap)
        res = []
        while maxHeap:
            
            count,key = heappop(maxHeap)
            res.append(key)
            
            count+=1
            
            if used:
                ele = used.pop()
                heappush(maxHeap,ele)
            
            if count < 0:
                used.append([count,key])
        
        if not used and not maxHeap:
            return ''.join(res)
        
        return ''
                
        
        