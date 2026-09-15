class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        memo = {}
        def dfs(amt):
            if amt == 0:
                return 0
            
            if amt < 0:
                return float("inf")
            if amt in memo:
                return memo[amt]

            minCoins = float("inf")
            for coin in coins:
                subProb = dfs(amt - coin)
                if subProb != float("inf"):
                    minCoins = min(minCoins, subProb + 1)
            memo[amt] = minCoins
            return memo[amt]

        res = dfs(amount)
        return -1 if res == float("inf") else res