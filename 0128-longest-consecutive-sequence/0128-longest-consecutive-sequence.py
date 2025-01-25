from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = list(set(nums)) # Get unique entries the non uniques are useless

        n = len(nums) 

        rank = [0]*n
        parent = [i for i in range(n)]
        
        def findParent(x):
            if parent[x] == x:
                return x
            parent[x] = findParent(parent[x])
            return parent[x]
        
        def merge(x,y):
            rootX, rootY = findParent(x), findParent(y)

            if rootX == rootY:
                return 
            else:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] +=1
        
        invertedIndex = {} # hashMap where we map value -> index 

        for index,ele in enumerate(nums):
            if ele+1 in invertedIndex:
                merge(index,invertedIndex[ele+1])
            if ele-1 in invertedIndex:
                merge(index,invertedIndex[ele-1])
            invertedIndex[ele] = index
        
        for i in range(n):
            parent[i] = findParent(i)

        ctr = Counter(parent)
        return max(list(ctr.values())) if ctr else 0
        


        