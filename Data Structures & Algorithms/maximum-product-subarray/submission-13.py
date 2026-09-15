class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        globalMax = curMin = curMax = nums[0]
        for idx, num in enumerate(nums[1:]):
            if num < 0:
                curMax, curMin = curMin, curMax

            curMax = max(num, num * curMax)
            curMin = min(num, num * curMin)
            globalMax = max(globalMax, curMax)
        return globalMax