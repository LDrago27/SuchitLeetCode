class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # ALl 0 that are connected with 0 edges can't be converted to X
        
        zeroList = []
        
        queue = []
        
        n,m = len(board), len(board[0])
        
        for i in range(n):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][-1] == 'O':
                queue.append((i,m-1))
                
        for j in range(1,m):
            if board[0][j] == 'O':
                queue.append((0,j))
            if board[-1][j] == 'O':
                queue.append((n-1,j))
                
        
        
        seen = set()
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            node = queue.pop(0)
            
            if node in seen:
                continue
                
            x,y = node
            seen.add(node)
            zeroList.append(node)
            
            for dx,dy in directions:
                newX,newY = x+dx, y+dy
                
                if newX<0 or newY<0 or newX>=n or newY>=m or board[newX][newY] == 'X' or (newX,newY) in seen:
                    continue
                
                queue.append((newX,newY))
                
        zeroList = set(zeroList)
        #print(zeroList)
        for i in range(n):
            for j in range(m):
                
                if board[i][j] == 'O':
                    if (i,j) not in zeroList:
                        board[i][j] = 'X'
                        
            
            
            