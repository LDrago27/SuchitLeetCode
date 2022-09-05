class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start,end = 0, len(nums)-1
        origArray =[]
        
        for num in nums:
            origArray.append(num)
                
        
        nums.sort()
        
        found = False
        
        while(start<end):
            currVal = nums[start]
            targetVal = target - currVal
            while targetVal < nums[end]:
                end = end -1
            if targetVal == nums[end]:
                found = True
                break
            
            start = start+1
        
        if found:
            startIndex = origArray.index(nums[start])
            endIndex = 0
            
            n = len(origArray)
            for i in range(n-1,-1,-1):
                if (origArray[i]==nums[end]):
                    endIndex = i
                    break
            
            return [startIndex,endIndex]
            
            
        
        
        