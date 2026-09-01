class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if not nums:
            return 0

        def dfs(i):
            if i == 1:
                return nums[0]
            
            if i == 2:
                return max(nums[0], nums[1])
            
            if i in dp:
                return dp[i]

            dp[i] = max(dfs(i - 2) + nums[i - 1], dfs(i - 1))
            return dp[i]

        return dfs(len(nums))
