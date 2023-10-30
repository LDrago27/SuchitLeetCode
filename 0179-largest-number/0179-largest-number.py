from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strNums = [str(ele) for ele in nums]
        
        def comparator(str1,str2):
            if str1+str2 < str2+str1:
                return -1
            else:
                return 1
        
        res = sorted(strNums, key=cmp_to_key(comparator), reverse = True)
        
        res = ''.join(res)
        
        i = 0
        n = len(res)
        while i<n and res[i]=='0':
            i+=1
            
        if i==n:
            return '0'
        else:
            return res[i:]
