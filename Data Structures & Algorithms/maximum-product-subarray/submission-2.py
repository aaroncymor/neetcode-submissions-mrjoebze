class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0
        l, r = 0, len(nums) - 1

        while l < len(nums):
            prefix = nums[l] * (prefix or 1)
            suffix = nums[r] * (suffix or 1)
            res = max(res, max(prefix, suffix))
            l += 1
            r -= 1
        return res