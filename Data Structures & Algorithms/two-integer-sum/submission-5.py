class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            hm[n] = i

        print(hm)
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hm and i != hm[complement]:
                return [i, hm[complement]]
        return []


