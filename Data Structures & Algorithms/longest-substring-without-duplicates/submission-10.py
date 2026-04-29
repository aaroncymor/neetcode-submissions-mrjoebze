class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                print("S[j]", s[j])
                if s[j] in charSet:
                    longest = max(longest, len(charSet))
                    break
                charSet.add(s[j])
        return longest
        