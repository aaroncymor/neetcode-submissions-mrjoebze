class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if nums[i] in hm:
                return [hm[nums[i]], i]
            hm[res] = i
