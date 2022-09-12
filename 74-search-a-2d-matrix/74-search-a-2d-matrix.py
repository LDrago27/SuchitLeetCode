class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we start with the top right element
        n,m = len(matrix),len(matrix[0])
        row,col = 0,m-1
        
        while row<n and col>=0:
            if target == matrix[row][col]:
                return True
            elif target> matrix[row][col]:
                row+=1
            else:
                col-=1
        return False