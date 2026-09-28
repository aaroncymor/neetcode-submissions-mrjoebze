class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prefix = suffix = 0
        maxProd = nums[0]

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - i - 1] * (suffix or 1)
            maxProd = max(maxProd, prefix, suffix)

        return maxProd