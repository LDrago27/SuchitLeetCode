class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd , minProd = 1, 1
        
        res = max(nums)
        # Idea is either we include the current element or not
        
        for ele in nums:
            tempMax = maxProd
            maxProd = max(ele*maxProd,ele*minProd,ele)
            minProd = min(ele*tempMax,ele*minProd,ele)
            res= max(res, maxProd)
            
        return res
                
        