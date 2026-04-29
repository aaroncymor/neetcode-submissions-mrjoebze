class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 2:
            return nums[1]

        total = 0
        def dfs(i):
            nonlocal total
            if (i > len(nums) - 1):
                return
            total += nums[i]
            dfs(i + 2)

        dfs(0)
        return total

