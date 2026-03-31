class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            curr = ""
            for j in range(i, len(s)):
                if s[j] in curr:
                    break
                curr += s[j]
                longest = max(longest, len(curr))
        return longest