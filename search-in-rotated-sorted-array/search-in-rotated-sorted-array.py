class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def findPivot(start,end):
            
            while start<=end:
                mid = (start+end)//2
                
                if mid<n-1 and nums[mid] > nums[mid+1]:
                    return mid+1
                if mid>0 and nums[mid-1] > nums[mid]:
                    return mid
                
                elif nums[mid] > nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            return 0
        
        def binarySearch(start,end,target):
            while start<=end:
                #print(start,end)

                mid = (start+end)//2
                
                if nums[mid] == target:
                    return mid
                
                if target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            return -1
            
        pivot = findPivot(0,n-1)
        print(pivot)
        start,end = 0,n-1
        if pivot ==0:
            return binarySearch(start,end,target)
        elif nums[pivot] == target:
            return pivot
        elif target >= nums[start]:
            return binarySearch(start,pivot-1,target)
        return binarySearch(pivot+1,end,target)