class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        currlongest = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                currlongest += 1
            elif nums[i] != nums[i - 1]:
                longest = max(longest, currlongest)
                currlongest = 1
        return max(longest, currlongest)


