class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for num in nums:
            tmp = max(n1+num, n2)
            n1 = n2
            n2 = tmp
        return n2