class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False