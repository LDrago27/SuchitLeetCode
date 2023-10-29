class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        # Idea is that each rabbits tell info abourt how many other are present with color different than itself
        # So we need to keep track of no elements we have seen sdo far 
        
        hashMap = {}
        res = 0
        for ele in answers:
            
            if ele in hashMap:
                hashMap[ele]-=1
                
                if hashMap[ele] == 0:
                    # we have seen all of the same color so we need to remove it
                    del hashMap[ele]
            else:
                res += ele+1 # including itself
                
                if ele != 0:
                    # no need to add it to the hashMap
                    hashMap[ele] = ele
                    
        return res