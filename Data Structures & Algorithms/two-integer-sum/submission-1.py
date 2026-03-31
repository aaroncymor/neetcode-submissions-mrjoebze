class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if target == (nums[i] + nums[j]):
                    return [i, j]
        return []
