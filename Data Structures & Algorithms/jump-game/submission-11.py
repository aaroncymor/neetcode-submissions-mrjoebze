class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = {}
        def can_reach(i):

            if i >= len(nums) - 1:
                return True
            
            if i in memo:
                return memo[i]

            jumps = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, jumps + 1):
                if can_reach(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False
        
        return can_reach(0)