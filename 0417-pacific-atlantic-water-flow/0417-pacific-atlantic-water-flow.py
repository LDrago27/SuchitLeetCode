class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()

        n,m = len(heights), len(heights[0])

        def dfs(currPos,visitedSet):
            x,y = currPos
            visitedSet.add(currPos)
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                newX,newY = x+dx, y+dy
                if newX >= n or newX<0 or newY>=m or newY<0 or (newX,newY) in visitedSet:
                    continue
                if heights[newX][newY] >= heights[x][y]:        
                    dfs((newX,newY), visitedSet)

        
        # Case 1: Find all elements that are reachable from pacific i.e the fiorst row and first column
        pacificSet = set()
        for j in range(m):
            pacificSet.add((0,j))
        for i in range(n):
            pacificSet.add((i,0))

        # Find all tiles reachable by this row 
        for startPos in pacificSet:
            if startPos not in pacific:
                dfs(startPos,pacific)

        # Case 2: Find all elements that are reachable from Atlantic i.e the fiorst row and first column
        atlanticSet = set()
        for j in range(m):
            atlanticSet.add((n-1,j))
        for i in range(n):
            atlanticSet.add((i,m-1))

        # Find all tiles reachable by this row 
        for startPos in atlanticSet:
            if startPos not in atlantic:
                dfs(startPos,atlantic)
        
        common = pacific.intersection(atlantic)
        res = []
        for ele in common:
            res.append(list(ele))
        
        return res

        


                


        