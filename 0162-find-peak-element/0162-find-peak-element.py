class Solution:
   def findPeakElement(self, arr: List[int]) -> int:
                
        n = len(arr)
        
        start,end = 0,n-1
        
        while start<=end:
            mid = (start+end)//2
            
            if mid>0 and arr[mid] < arr[mid-1]:
                end = mid -1
            elif mid<n-1 and arr[mid] <arr[mid+1]:
                start = mid+1
            else:
                return mid

        
            
            


     