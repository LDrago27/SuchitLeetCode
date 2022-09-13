class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n,m = len(box),len(box[0])
        
        rotateBox = [['.']*n for _ in range(m)]
        
        for i in range(n):
            fillStart = m-1
            for j in range(m-1,-1,-1):
                if box[i][j] == '#':
                    rotateBox[fillStart][n-1-i] = '#'
                    fillStart-=1
                elif box[i][j] == '*':
                    rotateBox[j][n-1-i] = '*'
                    fillStart = j-1
        return rotateBox