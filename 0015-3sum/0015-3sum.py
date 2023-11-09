class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        
        def twoSum(left,right,target):
            res = []
            while left < right and right >=0 and left<n:
                if nums[left]+ nums[right]== target:
                    res.append([nums[left],nums[right]])
                    left +=1
                    right-=1
                elif nums[left]+ nums[right] > target:
                    right-=1
                else:
                    left+=1
                    
            return res
        triplet = []
        for i in range(n):
            
            res = twoSum(i+1,n-1,-nums[i])
            
            for ele in res:
                if [nums[i]]+ele not in triplet:
                    triplet.append([nums[i]]+ele)
                
        return triplet
                    
                    