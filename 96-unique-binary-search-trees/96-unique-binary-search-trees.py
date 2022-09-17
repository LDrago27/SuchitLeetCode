class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}
        def createBSTUtil(start,end):
            
            if start>end:
                return 1
            else:
                res =0
                for i in range(start,end+1):
                    if (start,i-1) in cache:
                        leftSide = cache[(start,i-1)]
                    else:
                        leftSide = createBSTUtil(start,i-1)
                    
                    if (i+1,end) in cache:
                        rightSide = cache[(i+1,end)]
                    else:
                        rightSide = createBSTUtil(i+1,end)
                    
                    res+= leftSide * rightSide
                    
                cache[(start,end)] = res
                return res
        return createBSTUtil(1,n)
            