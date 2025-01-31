class TrieNode:
    def __init__(self,val):
        self.val = val
        self.child = {} # char -> TrieNode
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trieHead = TrieNode('') # -> Head 

    def addWord(self, word: str) -> None:
        head = self.trieHead

        for char in word:
            if char not in head.child:
                head.child[char] = TrieNode(char)
            head = head.child[char]
        
        head.end = True
        

    def search(self, word: str) -> bool:
        n = len(word)

        def util(currHead,index):
            if index == n:
                return True if currHead.end else False 
            char = word[index]
            if char != '.':
                return False if char not in currHead.child else util(currHead.child[char],index+1)
            else:
                keyList = list(currHead.child.keys())
                if not keyList:
                    return False
                else:
                    for key in keyList:
                        res = util(currHead.child[key],index+1)
                        if res: 
                            return True
                    return False
        return util(self.trieHead,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)