class Solution:
    def smallestFactorization(self, num: int) -> int:
        # This will only work if we can decompose the number into factors each of which are single digit in nature
        # Also we will need to see if we can reduce it further
        
        # idea is that we start with larer values and try to get lower values towrds the top to get the result
        
        base = 1
        res = 0
        
        if num < 2:
            return num
        
        for factor in range(9,1,-1):
            
            while num % factor == 0:
                num = num // factor
                res = res + base * factor
                base *=10
                
                     
        if num < 2 and res<2**31:
            return res
        return 0
                     
                
                     
                     
                     
            
        