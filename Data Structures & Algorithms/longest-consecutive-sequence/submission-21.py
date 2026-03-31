class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        longest = 0
        curr_longest = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                curr_longest += 1
            elif nums[i - 1] != nums[i]:
                longest = max(longest, curr_longest)
                curr_longest = 1
        return max(longest, curr_longest)

