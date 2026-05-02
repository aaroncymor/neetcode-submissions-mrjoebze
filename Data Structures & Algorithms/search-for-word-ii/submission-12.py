class PrefixTree:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixTree()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = PrefixTree()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, path = set(), set()
        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in path or board[r][c] not in node.children
            ):
                return
            
            path.add((r, c))
            node = node.children[board[r][c]]
            word = word + board[r][c]
            if node.word:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            path.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children and (r, c) not in path:
                    dfs(r, c, root, "")

        return list(res)
        