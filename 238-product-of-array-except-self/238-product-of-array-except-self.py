class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        leftSideProduct = [1]*n
        rightSideProduct = [1]*n
        
        for i in range(1,n):
            leftSideProduct[i] = leftSideProduct[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            rightSideProduct[i] = rightSideProduct[i+1] * nums[i+1]
        
        #print(leftSideProduct)
        #print(rightSideProduct)
        for i in range(n):
            nums[i] = leftSideProduct[i]*rightSideProduct[i]
            
        return nums