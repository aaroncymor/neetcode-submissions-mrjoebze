class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        numSet = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0 and (nums[i], nums[j], nums[k]) not in numSet:
                        numSet.add((nums[i], nums[j], nums[k]))
        return [list(n) for n in list(numSet)]





