from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        pairCounter = Counter(words)
        res = 0
        flag = False
        print(pairCounter)
        for word in words:
            
            if word[0]==word[1]:
                res += pairCounter[word]//2
                if pairCounter[word]%2!=0:
                    flag = True  
                pairCounter[word] = 0
            
            else:
                print('no')
                palin = word[::-1]
                if pairCounter.get(palin,0) and pairCounter.get(word,0):
                    res+= min(pairCounter.get(palin,0),pairCounter.get(word,0))
                    pairCounter[word] = 0
        print(res)
        res*=4
        if flag:
            res+=2
        return res
                
                