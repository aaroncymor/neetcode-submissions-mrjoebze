class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1
        numSet = set(nums)
        for i in range(len(nums)):
            curr_longest = 0
            curr_num = nums[i]
            while curr_num in numSet:
                curr_longest += 1
                curr_num += 1
            longest = max(longest, curr_longest)
        return longest



