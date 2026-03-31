class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visits.add((row, col))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (
                        r in range(ROWS) and c in range(COLS) and
                        (r, c) not in visits and grid[r][c] == "1"
                    ):
                        visits.add((r, c))
                        q.append((r, c))
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visits:
                    bfs(r, c)
                    islands += 1
        return islands