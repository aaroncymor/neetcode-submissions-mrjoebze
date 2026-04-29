class Solution:
    def wordSearch(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r >= ROWS or c >= COLS or r < 0 or c < 0 or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            path.add((r, c))
            result = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        for word in words:
            if self.wordSearch(board, word):
                res.append(word)
        return res

        