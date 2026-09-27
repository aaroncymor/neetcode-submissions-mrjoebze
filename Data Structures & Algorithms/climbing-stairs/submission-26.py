class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 0, 1
        for _ in range(n):
            tmp = one + two
            one = two
            two = tmp
        return two