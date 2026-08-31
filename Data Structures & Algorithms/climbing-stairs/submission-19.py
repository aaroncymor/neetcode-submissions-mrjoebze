class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i <= 0:
                return 0
            
            if i <= 2:
                return i
            
            if i in memo:
                return memo[i]
            
            memo[i] = dfs(i - 2) + dfs(i - 1)
            return memo[i]

        return dfs(n)