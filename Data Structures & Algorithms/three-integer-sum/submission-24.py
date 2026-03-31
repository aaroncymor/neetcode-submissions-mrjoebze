class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numSet = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if (nums[i], nums[j], nums[k]) not in numSet:
                            numSet.add((nums[i], nums[j], nums[k]))
        return [list(res) for res in list(numSet)]