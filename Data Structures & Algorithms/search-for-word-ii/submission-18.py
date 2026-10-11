class Trie:

    def __init__(self, *args, **kwargs):
        self.mapping = {}
        self.word = ""
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.mapping:
                cur.mapping[c] = Trie()
            cur = cur.mapping[c]
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for w in words:
            trie.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        res = set()
        def dfs(r, c, node):

            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or board[r][c] not in node.mapping
            ):
                return
            
            visited.add((r, c))
            ch = board[r][c]
            node = node.mapping[ch]
            if node.word:
                res.add(node.word)
            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and board[r][c] in trie.mapping:
                    dfs(r, c, trie)
        
        return list(res)