class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = {}

        if len(nums) == 2:
            memo[1] = max(nums[0], nums[1])
        
        def dfs(i):

            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i - 2) + nums[i], dfs(i - 1))
            print("MEMO", memo)
            return memo[i]
        
        return dfs(len(nums) - 1)