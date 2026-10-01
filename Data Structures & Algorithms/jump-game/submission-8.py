class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = {}
        def can_reach(i):

            if i >= len(nums) - 1:
                return True
                
            if i in memo:
                return memo[i]

            max_reach = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, max_reach + 1):
                if can_reach(j):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return can_reach(0)