class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        curr_longest = 0

        for num in nums:
            curr_num = num
            curr_longest = 1

            if curr_num - 1 in numSet:
                continue
            
            while curr_num + 1 in numSet:
                curr_num += 1
                curr_longest += 1
            longest = max(longest, curr_longest)
    
        return longest


