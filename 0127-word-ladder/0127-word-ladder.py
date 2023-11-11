from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Idea: Find the starting node from which we can get the shortest path 
        
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        
            
        def generateNextWord(word):
            n = len(word)
            res = []
            for i in range(n):
                for ele in 'abcdefghijklmnopqrstuvwxyz':
                    if ele!=word[i]:
                        res.append(word[:i]+ele+word[i+1:])
            return res+[word]
                        
        
        def findShortestPath(curr,target):
            if curr == target:
                return 0

            queue = [[curr,0]] # Using a BFs like tech
            seen = set()
            
            while queue:
                word,dist = queue.pop(0)
                if word == target:
                    return dist+1
                if word in seen:
                    continue
                seen.add(word)
                for nextWord in generateNextWord(word):
                    if nextWord in wordList and nextWord not in seen:
                        queue.append([nextWord,1+dist])
                        
            return float('inf')
        
        netRes = findShortestPath(beginWord,endWord)

        if netRes == float('inf'):
            return 0
        return netRes
        
        
            
            
            
            
        
        
        