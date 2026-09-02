class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
            
        q = deque([(amount, 0)])
        visited = set()
        visited.add(amount)
        while q:
            amt, steps = q.popleft()
            for c in coins:
                sub_problem = amt - c

                if sub_problem < 0:
                    continue

                if sub_problem in visited:
                    continue

                if sub_problem == 0:
                    return steps + 1
                
                q.append((amt - c, steps + 1))
                visited.add(amt - c)
        return -1