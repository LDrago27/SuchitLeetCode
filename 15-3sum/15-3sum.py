class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        def twoSum(start,end,target):
            val =[]
            while start<end:
                if nums[start]+nums[end]>target:
                    end= end-1
                elif nums[start]+nums[end]<target:
                    start= start+1
                else:
                    val.append([nums[start],nums[end]])
                    while start<end and nums[start]==nums[start+1]:
                        start= start+1
                    start= start+1
                    end= end-1
                    
            return val
        
        def ksum(k,target,arr,currIndex):
            #print(k,target,arr)
            if k==2:
                twoSumSets = twoSum(currIndex,n-1,target)
                for sets in twoSumSets:
                    res.append(arr+sets)
                return
            else:
                i=currIndex
                while i<n-k+1:
                    #print(i)
                    ksum(k-1,target-nums[i],arr+[nums[i]],i+1)
                    while i<n-1 and nums[i]==nums[i+1]:
                        #print("yo")
                        i= i+1
                    i=i+1
        ksum(3,0,[],0)       
        return (res)