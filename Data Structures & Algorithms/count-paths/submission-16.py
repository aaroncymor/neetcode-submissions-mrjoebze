class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for c in range(n):
            dp[0][c] = 1

        for r in range(m):
            dp[r][0] = 1

        q = deque([(1, 1)]) 

        while q:
            r, c = q.popleft()

            if r in range(m) and c in range(n) and dp[r][c] == 0:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                q.append((r + 1, c))
                q.append((r, c + 1))

        print("DP", dp)
        return dp[-1][-1]