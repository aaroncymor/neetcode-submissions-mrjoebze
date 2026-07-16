class Trie:
    def __init__(self):
        self.chars = {}
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.root = Trie()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = Trie()
            cur = cur.chars[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.chars:
                return False
            cur = cur.chars[c]
        return True