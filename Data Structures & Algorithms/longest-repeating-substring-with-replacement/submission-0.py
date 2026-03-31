class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)
        for c in charSet:
            count = 0
            left = 0
            for right in range(len(s)):
                if c == s[right]:
                    count += 1
                while (right - left + 1) - count > k:
                    if c == s[left]:
                        count -= 1
                    left += 1
                res = max(res, right - left + 1)
        return res

        