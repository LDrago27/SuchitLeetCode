class TrieNode:
    def __init__(self):
        self.child= {}
        self.endOfWord = False
class Solution:
    def findWords(self, board, words):
        
        # we can use a prefix Tree/ Trie to check if a word is present or not
        root = TrieNode()
        
        for word in words:
            start = root
            for char in word:
                if char not in start.child:
                    start.child[char] = TrieNode()
                start = start.child[char]
            start.endOfWord = True
        n1 = len(words)
        
        # we have prefix matching data structure
        n,m = len(board), len(board[0])
        visited = [[False]*m for _ in range(n)]
        res = []
        movement = [[-1,0],[1,0],[0,1],[0,-1]]
        
        def backTrack(currPos,trieNode,visited,currWord):
            if len(res) == n1:
                return
            x,y = currPos
            char = board[x][y]
            visited[x][y] = True
            currWord.append(char)
            if char in trieNode.child:
                trieNode = trieNode.child[char]
                if trieNode.endOfWord == True:
                    res.append(''.join(currWord))
                    trieNode.endOfWord= False
            
                for dx,dy in movement:
                    newX,newY = x+dx,y+dy
                    
                    if newX<0 or newX>=n or newY<0 or newY>=m  or visited[newX][newY]:
                        continue
                    
                    visited[newX][newY] = True
                    backTrack((newX,newY),trieNode, visited,currWord)
                    visited[newX][newY] = False
                currWord.pop()
            else:
                visited[x][y] = False
                currWord.pop()
                return
        
        for i in range(n):
            for j in range(m):
                if board[i][j] in root.child:
                    visited = [[False]*m for _ in range(n)]
                    backTrack((i,j),root,visited,[])
                if len(res) == n1:
                    break
        return res
            