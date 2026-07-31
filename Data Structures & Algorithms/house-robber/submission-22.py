class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        memo = {
            0: nums[0]
        }

        def dfs(n):

            if n < 0:
                return 0
            
            if n in memo:
                return memo[n]

            memo[n] = max(dfs(n - 1), dfs(n - 2) + nums[n])
            return memo[n]

        return dfs(len(nums) - 1)