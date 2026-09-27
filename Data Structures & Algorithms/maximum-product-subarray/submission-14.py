class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_max, cur_min, glob_max = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            if num < 0:
                # swap
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, num * cur_max)
            cur_min = min(num, num * cur_min)
            glob_max = max(glob_max, cur_max)
            
        return glob_max