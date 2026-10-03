class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums:
            return 0

        n = len(nums)
        max_reach = nums[0]

        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        
        return max_reach >= n - 1
