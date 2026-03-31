class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 1
        for i in range(len(nums)):
            currNum = nums[i]
            currLongest = 1
            if currNum - 1 in numSet:
                continue
            while currNum + 1 in numSet:
                currNum += 1
                currLongest += 1
            longest = max(longest, currLongest)
        return longest


