class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"
        N = len(t)
        P = [0] * N
        C, R = 0, 0

        for i in range(N):
            i_mirror = 2 * C - i
            if i < R:
                P[i] = min(R-i, P[i_mirror])
            
            while (
                i + P[i] + 1 < N and
                i - P[i] - 1 >= 0 and
                t[i + P[i] + 1] == t[i - P[i] - 1]
            ):
                P[i] += 1
            
            if i + P[i] > R:
                R = i + P[i]
                C = i
        
        center_idx = 0
        max_len = 0
        for i in range(len(P)):
            if max_len < P[i]:
                max_len = P[i]
                center_idx = i
        
        print("P", P)
        start = (center_idx - max_len) // 2
        return s[start: start + max_len]
