class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        
        one, two = 1, 1
        for _ in range(1, n):
            tmp = one + two
            one = two
            two = tmp
        return two
        