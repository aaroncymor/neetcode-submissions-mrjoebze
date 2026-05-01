class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        res = 0
        dp[0] = 0

        def dfs(a):
            if a == 0:
                return 0
            
            if dp[a] != -1:
                return dp[a]
            
            res = 1e9
            for c in coins:
                if a - c >= 0:
                    res = min(res, 1 + dfs(a - c))
            dp[a] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins