# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        
        n = reader.length()
        
        start,end = 0,n-1
        
        while start<end:
            
            mid = (start+end)//2
        
            if n%2 == 0:
                
                res = reader.compareSub(start,mid,mid+1,end)
                
                if res == 1:
                    end = mid
                elif res == -1:
                    start = mid+1

            else:
                res = reader.compareSub(start,mid-1,mid+1,end)
                if res == 1:
                    end = mid-1
                elif res == -1:
                    start = mid+1
                else:
                    return mid
                
            n = n//2

        return start

            

        
        
        
            
        
        