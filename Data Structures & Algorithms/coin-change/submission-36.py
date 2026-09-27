class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        visited = set()
        q = deque([(amount, 0)])
        visited.add(amount)

        while q:
            amt, lvl = q.popleft()
            for coin in coins:
                minCoins = amt - coin

                if minCoins < 0:
                    continue

                if minCoins in visited:
                    continue
                
                if minCoins == 0:
                    return lvl + 1
                
                q.append((minCoins, lvl + 1))
                visited.add(minCoins)
        return -1