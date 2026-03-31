class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False

        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False