class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.mapping = {}
                self.word = None
            
            def add(self, word):
                cur = self
                for c in word:
                    if c not in cur.mapping:
                        cur.mapping[c] = Trie()
                    cur = cur.mapping[c]
                cur.word = word
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()


        def dfs(r, c, visited, cur):
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] not in cur.mapping
            ):
                return
            visited.add((r, c))
            cur = cur.mapping[board[r][c]]
            if cur.word:
                res.add(cur.word)
            dfs(r + 1, c, visited, cur)
            dfs(r - 1, c, visited, cur)
            dfs(r, c + 1, visited, cur)
            dfs(r, c - 1, visited, cur)
            visited.remove((r, c))
        
        trie = Trie()
        for word in words:
            trie.add(word)
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and board[r][c] in trie.mapping:
                    dfs(r, c, visited, trie)
        
        return list(res)
            
