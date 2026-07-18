class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return False if not len(nums) > len(set(nums)) else True