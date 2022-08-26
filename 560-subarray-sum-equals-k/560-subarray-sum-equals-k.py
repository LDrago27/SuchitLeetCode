class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Anytime s8ubArray always think about prefix or cumulative sum
        # 0-i total till now is s we can make it k if we can remove a part s-k from it so that is the logic
        
        cache = {0:1}
        res = 0
        temp = 0
        
        for ele in nums:
            temp = temp+ele
            
            if temp - k in cache:
                res += cache[temp-k]
            
            cache[temp] = cache.get(temp,0)+1
        
        return res