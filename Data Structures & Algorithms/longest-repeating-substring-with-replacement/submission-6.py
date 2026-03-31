class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        track = {}
        for right in range(len(s)):
            c = s[right]
            track[c] = track.get(c, 0) + 1
            while (right - left + 1) - max(track.values()) > k:
                track[s[left]] -= 1
                left += 1
            longest = max(longest, (right - left + 1))
        return longest