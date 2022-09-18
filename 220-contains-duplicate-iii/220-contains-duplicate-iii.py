import math
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        
        # bucket sort method
        # indexDiff +1 size bucket
        
        maxBuckets = int(math.ceil((max(nums)-min(nums))/(valueDiff+1)))+1
        minEle = min(nums)
        bucket = [-1]*maxBuckets
        
        n = len(nums)
        
        for i in range(n):
            
            bucketNo = (nums[i]-minEle)//(valueDiff+1)

            #print(nums[i],bucketNo,bucket[bucketNo])
            if bucket[bucketNo]!=-1:
                return True
            
            if bucketNo>=1 and abs(bucket[bucketNo-1]!=-1 and abs(nums[i]-nums[bucket[bucketNo-1]])<=valueDiff):
                return True
            
            if bucketNo<maxBuckets-1 and abs(bucket[bucketNo+1]!=-1 and abs(nums[i]-nums[bucket[bucketNo+1]])<=valueDiff):
                return True
            
            bucket[bucketNo] = i
            #print(bucket[bucketNo])
            if i>=indexDiff:
                bucketNo = (nums[i-indexDiff]-minEle)//(valueDiff+1)
                bucket[bucketNo] = -1
        return False
            
            
            