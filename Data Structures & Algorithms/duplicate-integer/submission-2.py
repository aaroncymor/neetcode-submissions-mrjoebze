class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if num[i] == nums[j]:
                    return True
        return False