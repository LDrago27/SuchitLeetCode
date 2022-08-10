from heapq import heappop,heappush
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # have tewo heaps one maxheap and other minheap
        # keep the size of both heaps equal or differ by max 1 else to find the mdeian quickly
        # python has only support for min heap so max heap will be supported by -ve the number
        
        
        maxHeap = []
        minHeap = []
        
        n1, n2 = len(nums1), len(nums2)
        i,j = 0,0
        
        def maintainMedian(ele):
            if not maxHeap:
                heappush(maxHeap,ele*-1)
                return
            if not minHeap:
                heappush(minHeap,ele)
                return
            
            maxHeapTopEle = maxHeap[0]*-1
            minHeapTopEle = minHeap[0]
            
            if ele >= minHeapTopEle :
                heappush(minHeap,ele)
            else:
                heappush(maxHeap,ele*-1)
                
            # Rebalancing the heaps if they have diffrence of length > 1
            
            if len(minHeap)-len(maxHeap) >1:
                # minHeap has more no of elements so we need to remove the in element and add it to maxheap
                minEle =  heappop(minHeap)
                heappush(maxHeap,minEle*-1)
            elif len(maxHeap)-len(minHeap) >1:
                # maxHeap has more elements so we gonna remove one from it and add it to minHeap
                maxEle = heappop(maxHeap)*-1
                heappush(minHeap,maxEle)
        
        while i<n1 and j<n2:
            
            if nums1[i] <= nums2[j]:
                ele = nums1[i]
                i+=1
            else:
                ele = nums2[j]
                j+=1
            
            maintainMedian(ele)
        
        while i<n1:
            maintainMedian(nums1[i])
            i+=1
        
        while j<n2:
            maintainMedian(nums2[j])
            j+=1
        
        print(minHeap)
        print(maxHeap)
        if len(maxHeap) > len(minHeap):
            return maxHeap[0]*-1
        elif len(minHeap) > len(maxHeap):
            return minHeap[0]
        return (minHeap[0]+maxHeap[0]*-1)/2
                
            
            