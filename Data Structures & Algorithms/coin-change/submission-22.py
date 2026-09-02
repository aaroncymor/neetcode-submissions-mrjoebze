class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def minCoin(i):
            ctr = float("inf")
            
            if i == 0:
                return 0
            
            if i < 0:
                return float("inf")
            
            if i in dp:
                return dp[i]
            
            for c in coins:

                subProblem = minCoin(i - c)
                print(subProblem)
                if subProblem != float("inf"):
                    ctr = min(ctr, subProblem + 1)
            dp[i] = ctr
            return dp[i]
        
        res = minCoin(amount)
        print(res)
        return -1 if res == float("inf") else res