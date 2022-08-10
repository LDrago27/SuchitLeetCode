import math
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def countOfOne(x):
            count = 0
            orig = x
            while x:
                bit = x&1
                #print(bit)
                if bit:
                    count+=1
                x = x>>1
            return 10000*count+orig
        
        #print(countOfOne(1000))
        arr.sort(key = lambda x: countOfOne(x))
        return arr