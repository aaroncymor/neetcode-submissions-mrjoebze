class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = {}
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            longest = max(longest, (right - left + 1))
        return longest