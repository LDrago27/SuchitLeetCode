from heapq import heappop,heappush,heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we need to have 2 heaps one max heap for storing k elements and above second is min min heap storing element 
        self.minheap = []
        self.maxheap = [-ele for ele in nums]
        self.k = k
        heapify(self.maxheap)
        
        for i in range(k-1):
            ele = heappop(self.maxheap)*-1
            heappush(self.minheap,ele)
        


    def add(self, val: int) -> int:
            if len(self.minheap)<self.k-1:
                heappush(self.minheap,val)
                return 0

            elif len(self.maxheap) and val<= self.maxheap[0] *-1:
                return self.maxheap[0]*-1
            else:
                heappush(self.minheap,val)
                res = heappop(self.minheap)
                heappush(self.maxheap,res*-1)
                return res
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)