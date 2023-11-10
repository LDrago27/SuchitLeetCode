class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        
        
        def recurr(target,currEle,startIndex):
            if startIndex == n:
                return
            
            if target == 0:
                if currEle:
                    res.append(currEle)
                    
                return
            
            if target<0:
                return
            
            # Case 1 We use the curr element 
            recurr(target-candidates[startIndex],currEle+[candidates[startIndex]],startIndex)
            
            # Case 2 We don't use the curr element
            recurr(target,currEle,startIndex+1)
            
            
        recurr(target,[],0)
        return res

        