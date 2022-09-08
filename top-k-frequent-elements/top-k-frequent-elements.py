from random import randint
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # we can use quick select algorithm
        #i.e instead of selecting based on actual value we can make use of it's freq as a comapring factor
        
        count = {}
        
        for ele in nums:
            count[ele] = count.get(ele,0)+1
        
        # we have the counts now we need rearrage the keys so the most k
        keys = list(count.keys())
        
        def util(start,end,ksmall):
            # we will use quick select average O(N) worst case O(n^2)
            #print(keys)
            if ksmall == 0:
                return start-1
            
            pivot = (start+end)//2
            keys[pivot],keys[end] = keys[end],keys[pivot]
            
            ptr = start
            
            for i in range(start,end):
                if count[keys[i]] < count[keys[end]]:
                    keys[i],keys[ptr] = keys[ptr],keys[i]
                    ptr+=1
            #print(keys)
            keys[ptr],keys[end] = keys[end],keys[ptr]
            #print(keys)
            
            if  ptr-start+1 == ksmall:
                return ptr
            elif ptr-start+1 < ksmall:
                return util(ptr+1,end,ksmall-(ptr-start+1))
            else:
                return util(start,ptr-1,ksmall)
        n = len(keys)
        index = util(0,n-1,n-k)
        return keys[index+1:]
            
        
        