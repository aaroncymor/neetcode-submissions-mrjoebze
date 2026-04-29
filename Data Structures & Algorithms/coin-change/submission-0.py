class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minLen = float("inf")

        def dfs(i, counts, total):
            nonlocal minLen
            if amount == total:
                if minLen > len(counts):
                    minLen = len(counts)
                return
            
            if i >= len(coins) or total > amount:
                return
            
            counts.append(coins[i])
            dfs(i, counts, total + coins[i])
            counts.pop()
            dfs(i + 1, counts, total)
        
        dfs(0, [], 0)
        return -1 if minLen == float("inf") else minLen