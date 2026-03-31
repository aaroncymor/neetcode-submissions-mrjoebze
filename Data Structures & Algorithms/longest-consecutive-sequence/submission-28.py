class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {}
        for n in nums:
            seen[n] = 0
        
        def is_seen(n):
            if n not in seen:
                return 0
            if seen[n] == 0:
                seen[n] = is_seen(n - 1) + 1
            return seen[n]
        
        longest = 0
        for n in nums:
            longest = max(longest, is_seen(n))
        return longest

