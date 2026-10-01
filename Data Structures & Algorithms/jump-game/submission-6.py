class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        memo = {}
        max_reach = nums[0]

        def can_reach(i):
            nonlocal max_reach
            
            if i >= len(nums):
                return False

            if i == len(nums) - 1:
                return True

            if i in memo:
                return memo[i] 

            max_reach = max(max_reach, i + nums[i])
            for i in range(i + 1, max_reach + 1):
                if can_reach(i):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return can_reach(0)