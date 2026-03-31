class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        numSet = set(nums)
        longest = 1
        for n in nums:
            curr_longest = 1
            curr_num = n

            if curr_num - 1 in numSet:
                continue

            while curr_num + 1 in numSet:
                curr_num += 1
                curr_longest += 1

            longest = max(longest, curr_longest)

        return longest
