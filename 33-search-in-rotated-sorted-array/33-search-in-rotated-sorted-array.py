class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        def findPivot(start,end):
            # pivot is basically index of the smallest element
            
            mid = (start+end)//2
            
            if start>end:
                return -1
            
            if mid<end and nums[mid+1] < nums[mid]:
                return mid+1

            if start<mid and nums[mid-1] > nums[mid]:
                return mid
            print(start,mid)
            if nums[start] > nums[mid]:
                return findPivot(start,mid-1)
            return findPivot(mid+1,end)
        
        def binarySearch(start,end,target):
            
            if start>end:
                return -1
            
            mid= (start+end)//2
            
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                return binarySearch(mid+1,end,target)
            else:
                return binarySearch(start,mid-1,target)
            
        def searchWithPivot(start,end,target):
            pivot = findPivot(start,end)
            print(pivot)
            if start>end:
                return -1
            
            if pivot ==-1:
                return binarySearch(start,end,target)
            else:
                if nums[pivot] == target:
                    return pivot
                elif target >= nums[start]:
                    return binarySearch(start,pivot-1,target)
                return binarySearch(pivot+1,end,target)
        return searchWithPivot(0,n-1,target)