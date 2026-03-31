class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in nums:
            curr_num = num
            curr_longest = 1

            if num - 1 in num_set:
                continue

            while curr_num + 1 in num_set:
                curr_num += 1
                curr_longest += 1

            longest = max(longest, curr_longest)

        return longest