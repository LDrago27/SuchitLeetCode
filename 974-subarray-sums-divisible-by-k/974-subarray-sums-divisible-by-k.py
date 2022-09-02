class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        cache = {}
        
        temp = 0
        for ele in nums:
            temp += ele
            ind = temp%k
            cache[ind] = cache.get(ind,0)+1
            
        res = 0
        for key in cache:
            res +=  cache[key]*(cache[key]-1)//2
        res +=cache.get(0,0)
        
        return res
        