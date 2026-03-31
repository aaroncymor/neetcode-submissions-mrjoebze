class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = {}
        for n in nums:
            track[n] = 0

        def updateCount(n):
            if n not in track:
                return 0
            elif track[n] == 0:
                track[n] = updateCount(n - 1) + 1

            return track[n]

        longest = 0
        for n in nums:
            longest = max(longest, updateCount(n))
        return longest
