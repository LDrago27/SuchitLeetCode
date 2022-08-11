class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 10 9 2 5 3 7 101 18
        
        n = len(nums)
        dp = [1]*n
        
        for i in range(1,n):
            temp = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp,dp[j])
            dp[i] = 1 + temp
        print(dp)
        return max(dp)
    