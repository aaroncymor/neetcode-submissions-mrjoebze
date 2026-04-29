class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            if n in hm:
                return [i, hm[n]]
            hm[target - n] = i
        return []

