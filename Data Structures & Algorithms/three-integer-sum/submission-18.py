class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if (nums[i], nums[j], nums[k]) in res:
                            continue
                        res.append((nums[i], nums[j], nums[k]))

        return [list(nums) for nums in res]

