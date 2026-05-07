class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(a):
            if a == 0:
                return 0
            
            if a in memo:
                return memo[a]
            
            res = 1e9
            for c in coins:
                if a - c >= 0:
                    res = min(res, dfs(a - c) + 1)
            memo[a] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins