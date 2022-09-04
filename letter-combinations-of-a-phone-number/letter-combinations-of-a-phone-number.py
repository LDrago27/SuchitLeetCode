from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberTextmatrix = defaultdict(list)
        
        numberTextmatrix['2'] = ['a','b','c']
        numberTextmatrix['3'] = ['d','e','f']
        numberTextmatrix['4'] = ['g','h','i']
        numberTextmatrix['5'] = ['j','k','l']
        numberTextmatrix['6'] = ['m','n','o']
        numberTextmatrix['7'] = ['p','q','r','s']
        numberTextmatrix['8'] = ['t','u','v']
        numberTextmatrix['9'] = ['w','x','y','z']
        
        visitedmatrix = defaultdict(list)
        visitedmatrix['2'] = [False]*3
        visitedmatrix['3'] = [False]*3
        visitedmatrix['4'] = [False]*3
        visitedmatrix['5'] = [False]*3
        visitedmatrix['6'] = [False]*3
        visitedmatrix['7'] = [False]*4
        visitedmatrix['8'] = [False]*3
        visitedmatrix['9'] = [False]*4
        
        n = len(digits)
        res = []
        
        def recurr(i,arr):
            
            if i==n:
                if arr:
                    res.append(''.join(arr))
                return
            
            
            for char in numberTextmatrix[digits[i]]:
                recurr(i+1,arr+[char])
        
        recurr(0,[])
        return res
        
        