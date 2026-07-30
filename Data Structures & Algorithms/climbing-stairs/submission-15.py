class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 2}

        def fib(n):
            if n <= 0:
                return memo[0]
            
            if n in memo:
                return memo[n]
            
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
        
        return fib(n)