class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        def twoSum(start,end,target):
            
            res = []
            
            while start<end:
                
                if nums[start]+nums[end] > target:
                    end-=1
                elif nums[start]+nums[end]< target:
                    start+=1
                else:
                    res.append([nums[start],nums[end]])
                    start+=1
                    end-=1
            return res
        
        def util(start,end,k,target):
            if start>end or k==0:
                return []
            if k==2:
                return twoSum(start,end,target)
            else:
                res = []
                i = start
                while start<=end:
                    # we take nums[start] as one element and try to find other using it
                    res1 = util(start+1,end,k-1,target-nums[start])
                    print(res1)
                    if res1:
                        for val in res1:
                            res.append([nums[start]]+val)
                            
                    while start<end and nums[start+1]==nums[start]:
                        start+=1
                    
                    start+=1
                return res
            
        nums.sort()
        n = len(nums)

        res = util(0,n-1,3,0)
        tupleList = [(ele1,ele2,el3) for ele1,ele2,el3 in res]
        tupleSet = set(tupleList)
        return [[ele1,ele2,ele3] for ele1,ele2,ele3 in tupleSet]
        
                    
                