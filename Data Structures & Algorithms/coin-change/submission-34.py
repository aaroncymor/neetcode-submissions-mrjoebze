class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        q = deque([(amount, 0)])
        visited = set()
        visited.add(amount)

        while q:
            amt, minCoins = q.popleft()
            for coin in coins:
                if amt - coin in visited:
                    continue
                if amt - coin < 0:
                    continue
                if amt - coin == 0:
                    return minCoins + 1
                q.append((amt - coin, minCoins + 1))
                visited.add(amt - coin)
        return -1
                
