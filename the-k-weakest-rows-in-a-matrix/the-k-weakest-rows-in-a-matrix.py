class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        rowSum = [[i,sum(mat[i])] for i in range(n)]
        rowSum.sort(key = lambda x:x[1])
        return [rowSum[i][0] for i in range(k)]