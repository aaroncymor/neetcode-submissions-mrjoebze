class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_max_sum = nums[0]
        glob_max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_max_sum = max(nums[i], nums[i] + curr_max_sum)
            glob_max_sum = max(glob_max_sum, curr_max_sum)

        return glob_max_sum