class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordN = len(word)
        n = len(board)
        m = len(board[0])
        visited = [[False]*(m) for _ in range(n)]
         
        
        def recurr(startRow,startCol,index,visited):
            #print(startRow,startCol,index)
            
            if index == wordN or (index==wordN-1 and board[startRow][startCol]==word[index]):
                return True           
            
            visited[startRow][startCol] = True
            
            movement = [[-1,0],[1,0],[0,1],[0,-1]]
            
            if board[startRow][startCol] == word[index]:
                
                for dx,dy in movement:
                    newX,newY = startRow+dx,startCol+dy
                    
                    if newX <0 or newY<0 or newX>=n or newY>=m or visited[newX][newY]:
                        continue
                    
                    if recurr(newX,newY,index+1,visited):
                        return True
            visited[startRow][startCol] = False
            
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if recurr(i,j,0,visited):
                        return True
                    
        return False