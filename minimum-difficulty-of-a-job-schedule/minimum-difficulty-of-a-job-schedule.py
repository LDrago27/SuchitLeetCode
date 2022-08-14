class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        #we can have a recurrig method dp(i,day) day is date and i is the remaining job to be picked up
        
        n = len(jobDifficulty)
        
        if n<d:
            return -1
        
        dp = [[float('inf')]*(d+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][d] = max(jobDifficulty[i:])
        
        for i in range(n-1,-1,-1):
            for j in range(d-1,0,-1):
                
                tempDiff = float('inf')
                # on a day d we can can only check n-(D-j) jobs since we have ateleast compete one job each day
                maxJobPick = n - (d-j)
                mostDiff = 0
                for dj in range(maxJobPick+1):
                    if i+dj<n-1:
                        mostDiff = max(mostDiff,jobDifficulty[i+dj])
                        tempDiff = min(tempDiff, mostDiff + dp[i+dj+1][j+1])
                dp[i][j] = tempDiff
        print(dp)
        return dp[0][1]