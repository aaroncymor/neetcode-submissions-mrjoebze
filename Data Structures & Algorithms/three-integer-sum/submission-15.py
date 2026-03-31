class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numSet = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        numSet.add((nums[i], nums[j], nums[k]))
        return [list(item) for item in numSet]
