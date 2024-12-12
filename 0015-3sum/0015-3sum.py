class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        n = len(nums)
        res = set()
        
        def findTarget(start,end,target):
            if start >= end:
                return
            if nums[start]+nums[end] == target:
                res.add((-1*target,nums[start],nums[end]))
                return findTarget(start+1,end-1,target)
            elif nums[start]+nums[end] > target:
                return findTarget(start,end-1,target)
            else:
                return findTarget(start+1,end,target)
        i = 0
        while i<n:
            if nums[i] > 0:
                break
            findTarget(i+1,n-1,-1*nums[i])
            
            while i+1<n and nums[i+1]==nums[i]:
                i+=1 # Removes dupplicates
            
            i+=1
        
        # Convert set to list
        listRes= []
        
        for tup in res:
            listRes.append(list(tup))
            
        return listRes