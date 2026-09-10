class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = [-1, -1]
        for i in range(len(s)):
            l, r = i, i
            while r < len(s) and l >= 0:
                if s[l] != s[r]:
                    break
                if r - l + 1 > longest:
                    longest = r - l + 1
                    res = [l, r]
                r += 1
                l -= 1

            l, r = i, i + 1
            while r < len(s) and l >= 0:
                if s[l] != s[r]:
                    break
                if r - l + 1 > longest:
                    longest = r - l + 1
                    res = [l, r]
                r += 1
                l -= 1
        left, right = res
        return s[left:right + 1]