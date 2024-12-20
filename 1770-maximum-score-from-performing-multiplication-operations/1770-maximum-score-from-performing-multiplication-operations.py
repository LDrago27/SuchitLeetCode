class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # understanding the state variable we have three l,r and i(multiplier index)
        # but we can make do with only l and i r can be calculaed by n-1-i
        # r-l+1 = n-i or r = n-i+l-1
        # dp(l,i)
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):

                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])
        
        return dp[0][0]
                
        
        