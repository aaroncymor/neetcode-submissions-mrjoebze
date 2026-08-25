class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(i):
            if i == 0:
                return 0

            if i < 0:
                return float('inf')
            
            if i in dp:
                return dp[i]

            min_coins = float('inf')
            for c in coins:
                sub_problem = dfs(i - c)
                if sub_problem != float('inf'):
                    min_coins = min(min_coins, 1 + sub_problem)
            dp[i] = min_coins
            return dp[i]
        res = dfs(amount)
        return -1 if res == float('inf') else res