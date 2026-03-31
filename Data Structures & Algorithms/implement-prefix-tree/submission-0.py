class PrefixTree:

    def __init__(self):
        self.hashmap = {}
        self.words = []

    def insert(self, word: str) -> None:
        def dfs(i, hm):
            if not word or i >= len(word):
                return

            if word[i] not in hm:
                hm[word[i]] = {}

            dfs(i + 1, hm[word[i]])
        dfs(0, self.hashmap)
        self.words.append(word)

    def search(self, word: str) -> bool:
        if word not in self.words:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        def dfs(i, hm):
            if not prefix or i >= len(prefix):
                return True

            if prefix[i] not in hm:
                return False

            return dfs(i + 1, hm[prefix[i]])
        return dfs(0, self.hashmap)
        
        