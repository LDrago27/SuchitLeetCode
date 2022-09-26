from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #We will use a combination of dfs and bfs to solve this problem
        
        netWordsSet = set()
        graph = defaultdict(list)
        
        for word in wordList:
            netWordsSet.add(word)
            
        currLevel = {beginWord}
        depth = 0
        if endWord not in wordList:
            return depth
        
        while currLevel:
            nextLevel = set()
            netWordsSet = netWordsSet-currLevel
            depth+=1
            for word in currLevel:
                n = len(word)                
                if word==endWord:
                    return depth
                    
                for i in range(n):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i]+char+word[i+1:]
                        
                        if newWord in netWordsSet:
                            nextLevel.add(newWord)
                            graph[newWord].append(word)
            currLevel = nextLevel

            
        return 0
                            
                