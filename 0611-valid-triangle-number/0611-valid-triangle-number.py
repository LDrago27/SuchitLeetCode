from bisect import bisect_right
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
    # Fix the last pointer and try to find 2 other elements that can satisfy the condition
        nums.sort()

        n = len(nums)
        count = 0
        for lastIndex in range(n-1,1,-1):
            # so we have c we need a and b such that a+b > c
            c = nums[lastIndex]
            start,end = 0,lastIndex-1

            while start<end:

                if nums[start]==0:
                    start+=1

                elif nums[start]+nums[end] > c:
                    # So any start from [start,end) will staify this
                    count += end - start
                    end-=1
                else:
                    start+=1

        return count

                
                

        
        
