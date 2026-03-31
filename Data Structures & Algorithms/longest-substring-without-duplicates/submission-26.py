class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        charSet = set()
        left = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxL = max(maxL, len(charSet))
        return maxL