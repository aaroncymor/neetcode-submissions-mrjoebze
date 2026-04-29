class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        left = 0
        charSet = set()
        for right in range(len(s)):
            if s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxL = max(maxL, len(charSet))
        return maxL