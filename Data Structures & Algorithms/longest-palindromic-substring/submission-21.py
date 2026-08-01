class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        maxLen = 0
        left, right = -1, -1

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r <= len(s) - 1:

                if s[l] != s[r]:
                    break
                if maxLen < (r - l + 1):
                    maxLen = (r - l + 1)
                    left, right = l, r

                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1:

                if s[l] != s[r]:
                    break

                if maxLen < (r - l + 1):
                    maxLen = (r - l + 1)
                    left, right = l, r

                l -= 1
                r += 1
        
        return s[left: right + 1]