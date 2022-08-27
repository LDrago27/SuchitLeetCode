class Solution:
    def jump(self, nums: List[int]) -> int:
        # it can be seen as BFS we start at node  we need to find min ht to reachh the end node
        n = len(nums)
        start = 0
        maxLen = 0
        depth = 0
        
        while start<n and maxLen<n-1:
            
            tempLen = 0
            depth+=1
            while start<=n-2 and start<=maxLen:
                tempLen =  max(tempLen,start+nums[start])
                start+=1
            maxLen = tempLen
        #print(start)
        return depth
                    
                
        