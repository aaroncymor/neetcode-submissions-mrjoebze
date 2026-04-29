class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        longest = 0
        left = 0
        charSet = set()

        for right in range(len(s)):
            if s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            longest = max(longest, len(charSet))
        return longest
