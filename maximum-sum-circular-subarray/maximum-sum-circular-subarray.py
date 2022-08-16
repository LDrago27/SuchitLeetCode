class Solution(object):
    def maxSubarraySumCircular(self, arr):
        
        # 2 cases either the max is in the result of Kadan with -ve
        
        def kadan(arr):
            temp = 0
            maxEle = float('-inf')
            for ele in arr:
                temp+=ele
                maxEle = max(maxEle,temp)
                if temp<0:
                    temp = 0
            return maxEle
        
        case1Res = kadan(arr)
        case2Res = kadan([ele*-1 for ele in arr])
        
        count = 0
        for ele in arr:
            if ele <0:
                count+=1
        if count == len(arr):
            return case1Res
    
        
        return max(case1Res,sum(arr)+case2Res)
        
                