class Solution:
    def maximumSwap(self, num: int) -> int:
        # idea is we simply start with a element and check if we have an element higher than that whciohwe can replace it with 
        
        hashMap = {}
        
        num = list(str(num))
        
        for index,value in enumerate(num):
            
            hashMap[int(value)] = index
        n = len(num)
        for i in range(n):
            ele = int(num[i])
            
            for nextBigEle in range(9,ele,-1):
                
                if nextBigEle in hashMap and hashMap[nextBigEle] > i:
                    num[hashMap[nextBigEle]],num[i] = num[i],num[hashMap[nextBigEle]]
                    return int(''.join(num))
                
        return int(''.join(num))
        