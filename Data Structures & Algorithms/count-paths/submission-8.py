class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]

        def dfs(r, c):
            if r == 0 or c == 0:
                return 1
            
            if memo[r][c] != 0:
                return memo[r][c]
            
            if r < 0 or c < 0:
                return 0
            
            memo[r][c] = dfs(r - 1, c) + dfs(r, c - 1)
            return memo[r][c]
        
        return dfs(m - 1, n - 1)