class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not len(nums) or len(nums) == 1:
            return True

        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False