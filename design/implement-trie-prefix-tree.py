class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie
        for char in word:
            if char not in d:
                return False
            d = d[char]
        return '.' in d
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        for char in prefix:
            if char not in d:
                return False
            d = d[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)