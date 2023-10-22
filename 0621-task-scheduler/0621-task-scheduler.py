from collections import Counter
from heapq import heappop, heappush,heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # idea take a ctr of the tasks and arrange them in reverse order
        # alternate between the top elements untill everything is 0
        
        ctr = Counter(tasks)
        
        maxHeap = [] # of counts
        
        queue = [] # Track next time
        
        for key in ctr:
            maxHeap.append([ctr[key]*-1,key])
        
        heapify(maxHeap)
        time = 0
        while maxHeap or queue:
            
            if maxHeap:
                ctr,ele = heappop(maxHeap)
                # Now we decrement the counter
                ctr += 1
                
                # Now we update the next entry of the element
                if ctr < 0:
                    queue.append([time+n,key,ctr])
            
            # Checking if any time in queue is due its time
            if queue:
                if time >= queue[0][0]:
                    t,key,ctr = queue.pop(0)
                    heappush(maxHeap,[ctr,key])
            
            time+=1
        
        return time

            


        

        
        