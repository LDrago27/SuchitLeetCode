from heapq import heapify,heappush,heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n,m = len(matrix), len(matrix[0])
        
        pos1Row,pos1Col = 0 , 0
        minheap = []
        colNo = [1]*n
        for i in range(n):
            minheap.append([matrix[i][0],i])
        
        heapify(minheap)
        ctr = 0
        while ctr<k-1:
            minEle, rowNo = heappop(minheap)
            if colNo[rowNo]<m:
                heappush(minheap,[matrix[rowNo][colNo[rowNo]],rowNo])
                colNo[rowNo]+=1
            ctr+=1
        return minheap[0][0]
            