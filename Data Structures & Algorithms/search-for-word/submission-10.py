class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visits = set()

        def bfs(r, c):
            i = 0
            q = deque([(r, c)])

            while q:
                nr, nc = q.popleft()
                directions = [
                    [1, 0], [-1, 0], [0, 1], [0, -1]
                ]
                for dr, dc in directions:
                    r, c = nr + dr, nc + dc
                    if (
                        r in range(ROWS) and c in range(COLS) and
                        i < len(board) and board[r][c] == word[i] and 
                        (r, c) not in visits
                    ):
                        q.append((r, c))
                        visits.add((r, c))
                        i += 1

            if i == len(word):
                return True
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if bfs(r, c):
                    return True
        return False