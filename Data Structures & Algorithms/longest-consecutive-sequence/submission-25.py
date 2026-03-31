class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = 0
        
        def is_seen(num):
            if num not in seen:
                return 0
            elif seen[num] == 0:
                seen[num] = is_seen(num - 1) + 1
            return seen[num]
        
        longest = 0
        for num in nums:
            longest = max(longest, is_seen(num))
        print("SEEN", seen)
        return longest


