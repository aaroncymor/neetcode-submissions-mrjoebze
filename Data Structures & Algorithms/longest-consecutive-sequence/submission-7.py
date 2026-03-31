class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        num_set = set(nums)
        for i in range(len(nums)):
            curr_longest = 1
            curr_num = nums[i]

            if curr_num - 1 in num_set:
                continue

            while curr_num + 1 in num_set:
                curr_longest += 1
                curr_num += 1

            longest = max(longest, curr_longest)
        return longest



