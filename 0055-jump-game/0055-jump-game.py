class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        n = len(nums)
        for i in range(n):
            if maxReach < i:
                return False
            maxReach = max(maxReach,i+nums[i])
        return True