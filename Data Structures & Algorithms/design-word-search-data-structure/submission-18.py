class WordDictionary:

    def __init__(self):
        self.mapping = {}
        self.word_end = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.mapping:
                cur.mapping[c] = WordDictionary()
            cur = cur.mapping[c]
        cur.word_end = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.mapping.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.mapping:
                        return False
                    cur = cur.mapping[c]
            return cur.word_end
        return dfs(0, self)