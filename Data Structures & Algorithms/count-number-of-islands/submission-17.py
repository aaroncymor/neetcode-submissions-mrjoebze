class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def bfs(r, c):
            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == "1"
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands