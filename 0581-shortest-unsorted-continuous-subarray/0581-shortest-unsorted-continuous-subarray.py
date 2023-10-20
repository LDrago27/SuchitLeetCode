class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        # SO we need to find mismatch and keep on going till we get next one
        
        
        # Place each element in right position with index and we can check the index mismatch
        
        sortedArr = sorted(nums)
        
        indexMisMatch = []
        
        n = len(nums)
        
        for i in range(n):
            
            if nums[i]!=sortedArr[i]:
                indexMisMatch.append(i)
                
        if not indexMisMatch:
            return 0
        
        return indexMisMatch[-1]-indexMisMatch[0]+1
    
    

        
                        
                    
                
                
                
            
            
           

    
            