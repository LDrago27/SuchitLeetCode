class Solution:
    def removeInterval(self, intervals: List[List[int]], tobeRemoved: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        
        def lowerBound(target):
            
            start,end = 0,n-1
            
            while start<=end:
                mid = (start+end) // 2
                
                if target > intervals[mid][0]:
                    start = mid+1
                else:
                    end = mid-1
                    
            return end
        

            
        
        lowerBoundIndex = lowerBound(tobeRemoved[0])
        
        res = []
        
        for i in range(lowerBoundIndex):
            res.append(intervals[i])
        
        if intervals[lowerBoundIndex][1] <= tobeRemoved[0]:
            # So the lowerBoundIndex is non overlapping and should not be removed
            res.append(intervals[lowerBoundIndex])
        else:
            if (intervals[lowerBoundIndex][0]<tobeRemoved[0] ):
                res.append([intervals[lowerBoundIndex][0],tobeRemoved[0]])

        index = max(lowerBoundIndex,0)
        print(res)

        while index<n and tobeRemoved[1] > intervals[index][1]:
            index += 1
            
        if index<n and intervals[index][0]< tobeRemoved[1] < intervals[index][1]:
            res.append([tobeRemoved[1],intervals[index][1]])
            index +=1
            
        if index<n and tobeRemoved[1] == intervals[index][1]:
            index+=1
            
        for i in range(index,n):
            res.append(intervals[i])
            
        return res
            
                
            
            
        
        
            