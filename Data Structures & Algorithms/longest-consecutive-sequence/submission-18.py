class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        curr_longest = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                curr_longest += 1
            elif nums[i] != nums[i-1]:
                longest = max(curr_longest, longest)
                curr_longest = 1
        return max(longest, curr_longest)