class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amt):
            if amt == 0:
                return 0
            
            if amt < 0:
                return float("inf")
            
            if amt in dp:
                return dp[amt]

            minCoins = float("inf")
            for c in coins:
                subProblem = dfs(amt - c)
                if subProblem != float("inf"):
                    minCoins = min(minCoins, 1 + subProblem)
            dp[amt] = minCoins
            return dp[amt]

        res = dfs(amount)
        return -1 if res == float("inf") else res