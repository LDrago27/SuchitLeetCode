class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Idea we need to terack max and min of each partition if val is beyond that we change the paruition however if for any of the partition if we have a max and min that is less than any of previous then we return bad

            
        partStack = [[arr[0],arr[0]]]
        
        n = len(arr)
        
        for i in range(1,n):
            ele = arr[i]
            if ele >= partStack[-1][1]:
                partStack.append([ele,ele])
            
            else:
                maxValue, minValue = partStack[-1][1],ele
                
                while partStack and ele < partStack[-1][0]:
                    tmin, tmax = partStack.pop()
                    maxValue = max(tmax,maxValue)
                    minValue = min(tmin,minValue)
                
                if partStack and partStack[-1][1] <= ele:
                    partStack.append([ele,maxValue])
                elif partStack and partStack[-1][1] > ele:
                    partStack[-1][1] = maxValue
                else:
                    partStack.append([ele,maxValue])
            print(partStack)
        return len(partStack)

            
            
                 


                
            
                
                