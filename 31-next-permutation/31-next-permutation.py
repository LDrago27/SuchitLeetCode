from bisect import bisect_right
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# The structure is ___High___ we need to find the first index where the element is decreasing and replace it with just higher value in second half and then arrange the rest in ascending order


        n = len(nums)
        i = n-2
        while i>=0:
            if nums[i] < nums[i+1]:
                break
            i-=1
        
        # we need to swap i with just largest number of its right
        #IndexTwo = bisect_left(nums,i+1,n-1)
        
        tIndex = n-1
        while tIndex>i:
            if nums[tIndex] > nums[i]:
                break
            tIndex-=1
               
        
        temp =  nums[i]
        nums[i] = nums[tIndex]
        nums[tIndex] = temp
        
        nums[i+1:] = sorted(nums[i+1:])
        
        