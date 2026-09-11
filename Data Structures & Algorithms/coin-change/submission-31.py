class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        q = deque([(amount, 0)])
        visited = set()
        visited.add(amount)
        while q:
            a, lvl = q.popleft()
            for c in coins:
                min_coins = a - c
                if min_coins in visited:
                    continue
                
                if min_coins < 0:
                    continue
                
                if min_coins == 0:
                    return lvl + 1
                
                q.append((min_coins, lvl + 1))
                visited.add(min_coins)
        return -1
