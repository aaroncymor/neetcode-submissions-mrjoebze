class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1
        numSet = set(nums)
        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num - 1 not in numSet:
                continue
            curr_longest = 1
            while curr_num + 1 in numSet:
                curr_longest += 1
                curr_num += 1
            longest = max(longest, curr_longest + 1)

        return longest



