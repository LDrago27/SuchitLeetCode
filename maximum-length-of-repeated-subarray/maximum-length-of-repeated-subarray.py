class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        def recurr(index1,index2):
            if index1<0 or index2<0:
                return 0
            if nums1[index1]== nums2[index2]:
                return 1 + recurr(index1-1,index2-1)
            else:
                return max(recurr(index1-1,index2),recurr(index1,index2-1),recurr(index1-1,index2-1))
        n= len(nums1)
        m = len(nums2)
        
        dp= [[0]*(m+1)for _ in range(n+1)]
        res =0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums1[i-1] ==  nums2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    res= max(res,dp[i][j])
        
        return res
    