class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num - 1 in numSet:
                continue

            curr_longest = 1
            while curr_num + 1 in numSet:
                curr_num += 1
                curr_longest += 1

            longest = max(longest, curr_longest)
        return longest


