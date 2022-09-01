class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # since it is just the shortest we can directly make use of DFS
        
        wordSet = set(wordList)
        depth = 0
        
        if endWord not in wordSet:
            return 0
        
        currLevel = {beginWord}
        
        while currLevel:
            
            wordSet = wordSet - currLevel
            
            nextLevel = set()
            
            for word in currLevel:
                
                n = len(word)
                
                if word == endWord:
                    return depth+1
                
                for i in range(n):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i]+char+word[i+1:]
                        
                        if newWord in wordSet:
                            nextLevel.add(newWord)
            depth+=1
            currLevel = nextLevel
        return 0
            