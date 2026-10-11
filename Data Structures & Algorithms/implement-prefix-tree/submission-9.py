class PrefixTree:

    def __init__(self):
        self.map = {}
        self.end = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.map:
                cur.map[c] = PrefixTree()
            cur = cur.map[c]
        cur.end = True
            
    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.map:
                return False
            cur = cur.map[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.map:
                return False
            cur = cur.map[c]
        return True
        
        