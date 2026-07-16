class Trie:
    def __init__(self):
        self.chars = [None] * 26
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.root = Trie()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            key = ord(c) - ord('a')
            if not cur.chars[key]:
                cur.chars[key] = Trie()
            cur = cur.chars[key]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            key = ord(c) - ord('a')
            if not cur.chars[key]:
                return False
            cur = cur.chars[key]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            key = ord(c) - ord('a')
            if not cur.chars[key]:
                return False
            cur = cur.chars[key]
        return True