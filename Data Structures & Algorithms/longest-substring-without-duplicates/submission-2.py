class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 0
        for i in range(len(s)):
            charSet = set()
            charSet.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in charSet:
                    longest = max(longest, len(charSet))
                    break
                charSet.add(s[j])
        return longest
        