class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        freq = {}
           
        for right in range(len(s)):
            c = s[right]
            freq[c] = freq.get(c, 0) + 1
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, (right - left + 1))
        return longest