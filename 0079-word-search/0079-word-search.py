class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
           
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        wordLen = len(word)
        n,m = len(board), len(board[0])


        def util(boardCell, wordIndex, visited):
            x,y = boardCell
            if board[x][y] == word[wordIndex] and wordIndex == wordLen-1:
                return True
            if wordIndex >= wordLen or board[x][y]!=word[wordIndex]:
                return False

            visited.add(boardCell)
            for dx,dy in directions:
                newX,newY = x+dx,y+dy

                if newX <0 or newX>=n or newY<0 or newY>=m or (newX,newY) in visited:
                    continue
                    # invalid

                if util((newX,newY), wordIndex+1, visited):
                    return True
            visited.remove(boardCell)
            return False

        for i in range(n):
            for j in range(m):

                if board[i][j] == word[0]:
                    if (util((i,j),0,set())):
                        return True
        
        return False

