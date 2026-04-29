class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        totals = [0, 0]

        def dfs(i, x):
            if (i > len(nums) - 1):
                return
            totals[x] += nums[i]
            dfs(i + 2, x)

        dfs(0, 0)
        dfs(1, 1)
        return max(totals)

