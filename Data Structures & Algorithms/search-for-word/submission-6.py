class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i, target):
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in path or board[r][c] != word[i]
            ):
                return False

            target += word[i]
            if word == target:
                return True
            
            path.add((r, c))
            result = (
                dfs(r + 1, c, i + 1, target) or
                dfs(r - 1, c, i + 1, target) or
                dfs(r, c + 1, i + 1, target) or
                dfs(r, c - 1, i + 1, target)
            )
            path.remove((r, c))
            return result
        
        res = False
        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c, 0, "")
        return res

