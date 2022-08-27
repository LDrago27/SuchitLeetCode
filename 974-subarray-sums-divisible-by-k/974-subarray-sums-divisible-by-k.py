class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        cache = {}
        
        res = 0
        
        temp = 0
        
        for ele in nums:
            temp += ele 
            
            cache[temp%k] = cache.get(temp%k,0)+1
        
        for val in cache:
            res += cache[val]*(cache[val]-1)//2
        
        res+=cache.get(0,0)
        
        return res