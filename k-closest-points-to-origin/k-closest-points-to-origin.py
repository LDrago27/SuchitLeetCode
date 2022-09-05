class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        val = [[x,y,sqrt(x**2 + y**2)] for x,y in points]
        val.sort(key = lambda x: x[2])
        res = val[:k]
        return [[x,y] for x,y,d in res]
        
        