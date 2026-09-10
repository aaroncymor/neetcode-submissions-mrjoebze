class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        q = deque([(amount, 0)])
        visited = set()
        visited.add(amount)
        while q:
            amt, lvl = q.popleft()
            for coin in coins:
                minCoins = amt - coin
                if minCoins in visited:
                    continue

                if minCoins < 0:
                    continue

                if minCoins == 0:
                    return lvl + 1

                q.append((amt - coin, lvl + 1))
                visited.add(amt - coin)
        return -1