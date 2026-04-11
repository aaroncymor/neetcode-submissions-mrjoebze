class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        left, right = 0, 0
        for i in range(len(s)):
            l, r = i, i
            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                if resLen < r - l + 1:
                    resLen = r - l + 1
                    left, right = l, r
                l -= 1
                r += 1

            l, r = i, i + 1
            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                if resLen < r - l + 1:
                    resLen = r - l + 1
                    left, right = l, r
                l -= 1
                r += 1

        return s[left:right + 1]
