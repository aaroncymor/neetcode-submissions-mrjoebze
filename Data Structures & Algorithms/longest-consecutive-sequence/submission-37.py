class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        hmap = {}
        for num in nums:
            hmap[num] = 1
        
        def memo(n):
            if n not in hmap:
                return 0
            elif hmap[n] == 1:
                hmap[n] = memo(n - 1) + 1
            return hmap[n]
        
        longest = 0
        for num in nums:
            longest = max(longest, memo(num))
        return longest