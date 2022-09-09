class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        setA = set()
        setB = set([i for i in range(1,n+1)])
        
        # setA all number lower than i
        # setB all numbers higher than i
        # seat A is greater than 1  we good
        
        res = 0
        
        for i in range(1,n+1):
            if i in setB:
                setB.remove(i)
                setA.add(i)
            
            if flips[i-1] in setA:
                setA.remove(flips[i-1])
            elif flips[i-1] in setB:
                setB.remove(flips[i-1])
                
            if len(setA) == 0:
                res+=1
        return res