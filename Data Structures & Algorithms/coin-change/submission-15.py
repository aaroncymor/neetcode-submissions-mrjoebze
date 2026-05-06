class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount)
        seen[0] = True


        ctr = 0
        while q:
            ctr += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return ctr
                    
                    if nxt > amount or seen[nxt]:
                        continue
                    
                    seen[nxt] = True
                    q.append(nxt)
        return -1