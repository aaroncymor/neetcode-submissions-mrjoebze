class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_max = nums[0]
        global_max = nums[0]

        for num in nums[1:]:
            cur_max = max(num, num + cur_max)
            global_max = max(global_max, cur_max)
        return global_max