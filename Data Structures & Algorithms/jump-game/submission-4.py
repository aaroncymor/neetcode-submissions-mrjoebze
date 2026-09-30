class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if not nums:
            return True

        max_reach = nums[0]
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, nums[i] + i)

        return True if max_reach >= len(nums) - 1 else False
