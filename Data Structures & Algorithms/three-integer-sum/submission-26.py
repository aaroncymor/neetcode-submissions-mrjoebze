class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numSet = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        if (nums[i], nums[j], nums[k]) in numSet:
                            continue
                        numSet.add((nums[i], nums[j], nums[k]))

        return [list(r) for r in list(numSet)]

        