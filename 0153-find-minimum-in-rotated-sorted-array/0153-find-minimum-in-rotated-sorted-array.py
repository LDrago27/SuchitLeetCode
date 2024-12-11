class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def util(start,end):
            if (start==end):
                return nums[start]
            elif end-start==1:
                return min(nums[start],nums[end])
            mid = (start+end)//2
            
            # Is mid the min element
            if (mid>0 and mid<n-1 and nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]):
                return nums[mid]
    
            if (nums[mid] > nums[start] and nums[mid] < nums[end]):
                return util(start,mid-1)
            elif(nums[mid] > nums[start] and nums[mid] > nums[end]):
                return util(mid+1,end)
            else:
                return util(start,mid-1)
        return util(0,n-1)