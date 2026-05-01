class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            key = ord(c) - ord('a')
            if not cur.children[key]:
                cur.children[key] = TrieNode()
            cur = cur.children[key]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            key = ord(c) - ord('a')
            if not cur.children[key]:
                return False
            cur = cur.children[key]
        return cur.word
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            key = ord(c) - ord('a')
            if not cur.children[key]:
                return False
            cur = cur.children[key]
        return True