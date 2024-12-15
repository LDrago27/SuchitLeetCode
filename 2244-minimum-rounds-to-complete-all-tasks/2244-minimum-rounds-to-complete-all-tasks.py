from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        # Adding memomization to resolve the memory porblem
        cache = {}
        def roundToComplete(n):
            if n in cache:
                return cache[n]
            if n==0:
                return 0
            if n < 0:
                return float('inf')
            
            cache[n] = 1 + min(roundToComplete(n-2),roundToComplete(n-3))
            return cache[n]
        
        ctr = Counter(tasks)
        netRes = 0
        for key in ctr:
            res = roundToComplete(ctr[key])
            if res == float('inf'):
                return -1
            netRes += res
            
        return netRes