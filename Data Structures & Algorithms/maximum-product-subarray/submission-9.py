class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        prefix = suffix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - i - 1] * (suffix or 1)
            res = max(res, prefix, suffix)
        return res
