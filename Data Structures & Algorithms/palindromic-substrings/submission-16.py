class Solution:
    def countSubstrings(self, s: str) -> int:
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
                p[i] = min(R-i, p[i_mirror])
            
            while (
                (i + 1 + p[i]) < n and 
                (i - 1 - p[i]) > -1 and
                t[i + 1 + p[i]] == t[i - 1 - p[i]]
            ):
                p[i] += 1
            
            if i + p[i] > R:
                C = i
                R = i + p[i]

        total = sum([(val + 1) // 2 for val in p])
        return total