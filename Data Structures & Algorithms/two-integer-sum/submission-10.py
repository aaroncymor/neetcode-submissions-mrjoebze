class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                return [hm[nums[i]], i]
            key = target - nums[i]
            hm[key] = i