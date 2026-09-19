class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for c in range(n):
            grid[0][c] = 1

        for r in range(m):
            grid[r][0] = 1
        
        q = deque([(1, 1)])
        while q:
            r, c = q.popleft()
            
            if r >= m or c >= n:
                continue

            if grid[r][c] == 0:
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
                q.append((r + 1, c))
                q.append((r, c + 1))

        return grid[-1][-1]