class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not amount:
            return 0

        dp = {}

        def dfs(amt):

            if amt == 0:
                return 0
            
            if amt < 0:
                return float("inf")
            if amt in dp:
                return dp[amt]

            min_coins = float("inf")
            for c in coins:
                sub_problem = dfs(amt - c)
                if sub_problem != float("inf"):
                    min_coins = min(min_coins, 1 + sub_problem)
            dp[amt] = min_coins
            return min_coins
        
        res = dfs(amount)
        return -1 if res == float("inf") else res