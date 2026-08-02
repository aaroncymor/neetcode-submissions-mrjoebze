class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        C = 0
        R = 0

        for i in range(1, n - 1):
            i_mirror = (2 * C) - i
            if i < R:
                p[i] = min(p[i_mirror], R - i)
            
            while (
                (i + 1 + p[i] <= n - 1) and
                (i - 1 - p[i] >= 0) and 
                t[i + 1 + p[i]] == t[i - 1 - p[i]]
            ):
                p[i] += 1
            
            if i + p[i] > R:
                C = i
                R = i + p[i]
        
        print("P", p)
        center_idx = 0
        max_len = 0
        for idx, score in enumerate(p):
            if max_len < score:
                max_len = score
                center_idx = idx
        print(center_idx)
        print(max_len)
        
        start = (center_idx - max_len) // 2
        return s[start:start + max_len]
