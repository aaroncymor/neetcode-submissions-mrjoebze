class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            cur = nums[i]
            res = max(cur, res)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(cur, res)
        return res