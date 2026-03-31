class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            count[c] = count.get(c, 0) + 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest


        