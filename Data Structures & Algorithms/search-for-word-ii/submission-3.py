class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        visits = set()
        res = set()

        def dfs(r, c, node, word):
            if (
                c < 0 or r < 0 or c >= COLS or r >= ROWS
                or board[r][c] not in node.children
                or (r, c) in visits
            ):
                return
            
            visits.add((r, c))
            node = node.children[board[r][c]]
            word = word + board[r][c]
            if node.endOfWord:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visits.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
