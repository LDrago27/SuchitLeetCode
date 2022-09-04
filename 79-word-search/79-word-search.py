class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wl = len(word)
        visited =[[False]*n for i in range(m)]
        currRow = 0 
        currCol = 0
        
        def solutionPresent(currRow,currCol, visited,wordIndex):
            if wordIndex == wl:
                return True
            
            if currRow<0 or currRow>=m or currCol<0 or currCol>=n or board[currRow][currCol]!=word[wordIndex] or visited[currRow][currCol]:
                return False
            
            visited[currRow][currCol] = True
            res = (solutionPresent(currRow+1,currCol, visited,wordIndex+1) or
                    solutionPresent(currRow-1,currCol, visited,wordIndex+1) or solutionPresent(currRow,currCol+1, visited,wordIndex+1) or solutionPresent(currRow,currCol-1, visited,wordIndex+1))
            visited[currRow][currCol] = False
            
            return res                    
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and solutionPresent(i,j, visited,0):
                    return True
        return False
            