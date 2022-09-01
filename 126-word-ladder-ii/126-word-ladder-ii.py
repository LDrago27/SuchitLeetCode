from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        parent = defaultdict(list)
        
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return []
        
        currLevel = {beginWord}
        
        # BFS complete linked all the nodes amongst themselves
        while currLevel:
            wordSet = wordSet - currLevel
            
            nextLevel = set()
            
            for word in currLevel:
                n = len(word)
                for i in range(n):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + char +word[i+1:]
                        if newWord in wordSet:
                            nextLevel.add(newWord)
                            parent[newWord].append(word)
            
            currLevel = nextLevel
        
        
        res = []
        
        def dfs(word,path):
            if word == beginWord:
                path.append(beginWord)
                res.append(path[::-1])
                return
            else:
                
                for parentWord in parent[word]:
                    dfs(parentWord,path+[word])
        dfs(endWord,[])
        return res
                
        