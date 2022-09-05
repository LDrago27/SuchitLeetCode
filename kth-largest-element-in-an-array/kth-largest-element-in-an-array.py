class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
         # we will have a pivot and arrange elements on both side such that they are smaller and larger than each other 
         # kth largest is n-k smallest number
        
        
        def util(start,end,nsmallNumber):
            pivot  = (start+end)//2
            #print(start,end,nsmallNumber)
            nums[pivot],nums[end] = nums[end],nums[pivot]
            
            ptr = start
            
            for i in range(start,end):
                if nums[i] < nums[end]:
                    nums[ptr],nums[i] = nums[i],nums[ptr]
                    ptr+=1
            
            nums[ptr],nums[end] = nums[end],nums[ptr]
            #print(nums)
            
            # so now all elements below ptr are smaller than pivot
            if nsmallNumber == ptr-start+1:
                return nums[ptr]
            
            elif nsmallNumber > ptr-start:
                # we need to search in the second half
                return util(ptr+1,end,nsmallNumber-(ptr-start+1))
            else:
                return util(start,ptr-1,nsmallNumber)
        n = len(nums)
        return util(0,n-1,n-k+1)
            