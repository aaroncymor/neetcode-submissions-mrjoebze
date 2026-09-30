class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_max_sum, glob_sum = nums[0], nums[0]
        for num in nums[1:]:
            cur_max_sum = max(num, num + cur_max_sum)
            glob_sum = max(glob_sum, cur_max_sum)

        return glob_sum