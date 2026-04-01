class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visits.add((r, c))

            while q:
                nr, nc = q.popleft()
                directions = [
                    [1, 0], [-1, 0], [0, 1], [0, -1]
                ]
                for dr, dc in directions:
                    r, c = nr + dr, nc + dc
                    if (
                        r in range(ROWS) and c in range(COLS) and
                        (r, c) not in visits and grid[r][c] == "1"
                    ):
                        q.append((r, c))
                        visits.add((r, c))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visits and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands
