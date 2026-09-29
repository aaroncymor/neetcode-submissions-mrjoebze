class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]
        def dfs(r, c):
            if r == 0 or c == 0:
                dp[r][c] = 1
                return 1

            if dp[r][c]:
                return dp[r][c]
            
            if (
                r < 0 or c < 0 or c >= n or r >= m
            ):
                return 0
            
            dp[r][c] = dfs(r - 1, c) + dfs(r, c - 1)
            return dp[r][c]

        dfs(m - 1, n - 1)
        print("DP", dp)
        return dp[-1][-1]