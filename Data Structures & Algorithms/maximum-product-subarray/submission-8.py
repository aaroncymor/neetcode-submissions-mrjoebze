class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        global_max, cur_max, cur_min = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:  # negative num
                cur_max, cur_min = cur_min, cur_max
                
            cur_max = max(nums[i], nums[i] * cur_max)
            cur_min = min(nums[i], nums[i] * cur_min)
            global_max = max(global_max, cur_max)
        return global_max