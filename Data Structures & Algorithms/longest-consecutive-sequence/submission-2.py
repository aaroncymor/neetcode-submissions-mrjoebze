class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 1
        curr_longest = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_longest += 1
            elif nums[i] != nums[i - 1]:
                longest = max(longest, curr_longest)
                curr_longest = 1
        return max(longest, curr_longest)

