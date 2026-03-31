class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            maxL = max(maxL, len(charSet))
        return maxL
