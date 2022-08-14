class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key = lambda x: len(x))
        cache = {}
        
        def recurr(s):
            if len(s) == 0:
                return True
            if len(s)< len(wordDict[0]):
                    return False
                
            if s not in cache:
                res = False

                for word in wordDict:
                    n = len(word)
                    if n > len(s):
                        break
                    if word == s[:n]:
                        if recurr(s[n:]):
                            res = True
                            break
                cache[s] = res
            return cache[s]
        
        return recurr(s)