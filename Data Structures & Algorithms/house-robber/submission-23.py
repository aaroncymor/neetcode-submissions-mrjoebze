class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        memo = {}

        def dfs(i):
            if i == 0:
                return nums[0]
            
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i-2)+nums[i],dfs(i-1))
            return memo[i]
        return dfs(len(nums)-1)