from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        countOfNums = Counter(nums)
        uniqueNums = list(set(nums))
        uniqueNums.sort()
        
        n = len(uniqueNums)
        
        coins = [0]*n
        coins[0] = uniqueNums[0]*countOfNums[uniqueNums[0]]
        if n!=1:
            for i in range(1,n):
                if uniqueNums[i-1]+1==uniqueNums[i]:
                    if i==1:
                        coins[i] = max(coins[i-1],uniqueNums[i]*countOfNums[uniqueNums[i]]) 
                    else:
                        coins[i] = max(coins[i-1],uniqueNums[i]*countOfNums[uniqueNums[i]]+coins[i-2])
                else:
                    coins[i] = max(coins[i-1],uniqueNums[i]*countOfNums[uniqueNums[i]]+coins[i-1])
        print(coins)
        return coins[-1]
        
        
        
        