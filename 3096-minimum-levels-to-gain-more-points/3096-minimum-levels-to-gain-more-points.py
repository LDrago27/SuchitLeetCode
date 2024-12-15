class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
                
        possible = [1 if x == 1 else -1 for x in possible]
        n = len(possible)
        netSum = sum(possible)
        
        currSum = 0
        for index,value in enumerate(possible):
            
            currSum += value
            if currSum > netSum-currSum and index!=n-1:
                # Avoid the scenario where Bob can't play any moves
                return index+1
            
        return -1