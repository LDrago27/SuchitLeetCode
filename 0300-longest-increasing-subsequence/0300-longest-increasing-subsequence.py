from heapq import heappop,heappush,heapify
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n # themseleves
        
        '''
        # For each current value we need find elememts  smaller than it increment it
        # O(n^2) -> Time space O(n)
        for i in range(1,n):
            temp = dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp,dp[j]+1)
            dp[i] = max(dp[i],temp)
        '''
        minHeap = [[nums[0],0]]
        for i in range(1,n):
            temp = dp[i]
            popedEle = []
            while minHeap and nums[i] > minHeap[0][0]:
                ele = heappop(minHeap)
                temp = max(temp,dp[ele[1]]+1)
                popedEle.append(ele)
            
            dp[i] = max(dp[i],temp)
            minHeap = popedEle + minHeap # Since the poipedEle are already in order so we are not chagning it 
            heapify(minHeap)
            heappush(minHeap,[nums[i],i])
         
        return max(dp)
            
        
        
        
        return max(dp)
            
                
        