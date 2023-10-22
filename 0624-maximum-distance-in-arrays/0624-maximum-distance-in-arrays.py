class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        maxArr = []
        minArr = []
        
        for i,arr in enumerate(arrays):
            maxArr.append([arr[-1],i])
            minArr.append([arr[0],i])
            
        maxArr.sort(reverse = True)
        minArr.sort()
        
        if maxArr[0][1] == minArr[0][1]:
            return max(abs(maxArr[0][0]-minArr[1][0]),abs(maxArr[1][0]-minArr[0][0]))
        else:
            return max(abs(maxArr[0][0]-minArr[0][0]),abs(maxArr[0][0]-minArr[1][0]),abs(maxArr[1][0]-minArr[0][0]))
        
        
        
            
        
        