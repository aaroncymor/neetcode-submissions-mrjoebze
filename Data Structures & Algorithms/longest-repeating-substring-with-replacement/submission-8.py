class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0
        window = {}
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            maxL = max(maxL, right - left + 1)
        return maxL