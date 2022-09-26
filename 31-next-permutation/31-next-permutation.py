class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # fiundamentals are simple
        # fiind the pivot
        # second find the smallest before it and samllest number after it swap them
        # sort thee numbers after the pivot
        
        # find the pivot
        n = len(nums)
        i = n-2
        
        while i>=0:
            if nums[i+1]>nums[i]:
                break
            i-=1
        
        # now we need to find an element just higher than pivot
        pivot = i
        i = n-1
        while i>pivot:
            if nums[i]>nums[pivot]:
                break
            i-=1
            
        nums[i],nums[pivot] = nums[pivot],nums[i]
        print(nums,pivot,i)
        nums[pivot+1:] = sorted(nums[pivot+1:])
        
        
        
        