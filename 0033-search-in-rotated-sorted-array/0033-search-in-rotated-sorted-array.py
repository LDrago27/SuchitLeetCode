class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        def findPivot(start,end):
            if start==end:
                return start
            mid = (start+end)//2
            if nums[mid] > nums[end]:
                return findPivot(mid+1,end)
            else:
                return findPivot(start,mid)
        
        def binarySearch(start,end):
            if start > end:
                return -1
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(start,mid-1)
            else:
                return binarySearch(mid+1,end)
            
        pivot = findPivot(0,n-1)        
        
        if target > nums[-1]:
            return binarySearch(0,pivot-1)
        else:
            return binarySearch(pivot,n-1)
        
        
        
        
        