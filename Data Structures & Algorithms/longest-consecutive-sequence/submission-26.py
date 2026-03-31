class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in nums:
            curr_num = n
            if curr_num - 1 in numSet:
                continue
            
            curr_longest = 1
            while curr_num + 1 in numSet:
                curr_num += 1
                curr_longest += 1
            
            longest = max(longest, curr_longest)
        return longest