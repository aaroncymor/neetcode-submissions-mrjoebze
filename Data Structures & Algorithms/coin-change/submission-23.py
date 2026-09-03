class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        q = deque([(amount, 0)])
        visited = set()
        visited.add(amount)
        while q:
            amt, step = q.popleft()
            for c in coins:
                new_amt = amt - c

                if new_amt < 0:
                    continue

                if new_amt in visited:
                    continue
                
                if new_amt == 0:
                    return step + 1
                
                q.append((new_amt, step + 1))
                visited.add(new_amt)
        return -1