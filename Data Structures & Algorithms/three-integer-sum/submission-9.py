class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i - 1] == a:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + a
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[left], nums[right], a])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res




