class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 in numSet:
                continue
            
            curr_num = num
            curr_longest = 1
            while curr_num + 1 in numSet:
                curr_longest += 1
                curr_num += 1
            longest = max(longest, curr_longest)
        return longest