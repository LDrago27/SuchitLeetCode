class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        n = len(candidates)
        
        
        def recurr(target,currEle,startIndex):
            if target == 0:
                if currEle:
                    res.append(currEle)
                return
            
            if startIndex == n:
                return
            

            
            if target <0:
                return 
            
            # Case 1 Use the current element
            recurr(target-candidates[startIndex],currEle+[candidates[startIndex]],startIndex+1)
            
            # Case 2 Not use the current Element
            # So we need to find a different ndelement since if we find an element equat to currEle it is just goinfg to be same
            
            temp = startIndex+1
            
            while temp<n and candidates[temp]==candidates[startIndex]:
                temp+=1
                
            
            recurr(target,currEle,temp)
            
        recurr(target,[],0)
        
        return res
