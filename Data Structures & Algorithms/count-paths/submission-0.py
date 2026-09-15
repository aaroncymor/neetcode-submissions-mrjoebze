class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        ROWS, COLS = m, n

        for r in range(ROWS):
            dp[r][0] = 1
        
        for c in range(COLS):
            dp[0][c] = 1
        
        q = deque([(1, 1)])
        while q:
            r, c = q.popleft()
            if (
                r in range(ROWS) and (r - 1) in range(ROWS) and
                c in range(COLS) and (c - 1) in range(COLS) and
                dp[r][c] == 0
            ):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                q.append((r + 1, c))
                q.append((r, c + 1))
        
        print("DP", dp)
        return dp[-1][-1]