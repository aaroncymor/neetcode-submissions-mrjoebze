class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = "#" + "#".join(s) + "#"
            n = len(t)
            p = [0] * n
            r, l = 0, 0

            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (
                    (i + p[i] + 1 < n and i - p[i] - 1 >= 0) and
                    (t[i + p[i] + 1] == t[i - p[i] - 1])
                ):
                    p[i] += 1
            
            if i + p[i] > r:
                l, r = i - p[i], i + p[i]
            
            return p
        
        p = manacher(s)
        resLen, centerIdx = max((v, i) for i, v in enumerate(p))
        resIdx = (centerIdx - resLen) // 2
        print("CENTER IDX", centerIdx, "RES IDX", resIdx)
        print(resLen)
        return s[resIdx: resIdx + resLen]