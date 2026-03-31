class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
                longest = max(longest, len(charSet))
        return longest
        