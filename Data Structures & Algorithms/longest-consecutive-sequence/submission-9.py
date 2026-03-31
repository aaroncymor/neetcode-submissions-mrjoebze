class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        searched = {n: 0 for n in nums}

        def longestConsecutiveEnding(n):
            if n not in searched:
                return 0
            elif searched[n] == 0:
                searched[n] = longestConsecutiveEnding(n - 1) + 1
            return searched[n]

        longest = 0
        for n in nums:
            longest = max(longest, longestConsecutiveEnding(n))
        return longest




