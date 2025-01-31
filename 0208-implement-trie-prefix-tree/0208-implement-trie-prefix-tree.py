class TrieNode:
    def __init__(self,val):
        self.val = val
        self.child = {} # char -> TrieNode
        self.end = False
class Trie:

    def __init__(self):
        self.trieHead = TrieNode('') # -> Start Node 

    def insert(self, word: str) -> None:

        head = self.trieHead

        for char in word:

            if char not in head.child:
                head.child[char] = TrieNode(char)
            head = head.child[char]
        
        head.end = True



    def search(self, word: str) -> bool:
        
        head = self.trieHead

        for char in word:
            if char not in head.child:
                return False
            head = head.child[char]
        
        return True if head.end else False

    def startsWith(self, prefix: str) -> bool:

        head = self.trieHead

        for char in prefix:
            if char not in head.child:
                return False
            head = head.child[char]
        
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)