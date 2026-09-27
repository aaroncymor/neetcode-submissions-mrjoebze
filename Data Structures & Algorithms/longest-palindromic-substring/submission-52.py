class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"
        N = len(t)
        P = [0] * N
        R, C = 0, 0

        for i in range(N):
            i_mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[i_mirror])
            
            while (
                i + 1 + P[i] < N and
                i - 1 - P[i] >= 0 and
                t[i - 1 - P[i]] == t[i + 1 + P[i]]
            ):
                P[i] += 1
            
            if i + P[i] > R:
                C = i
                R = i + P[i]
        
        centerIdx, maxLen = 0, 0
        for i, n in enumerate(P):
            if maxLen < P[i]:
                maxLen = P[i]
                centerIdx = i
        
        startIdx = (centerIdx - maxLen) // 2
        return s[startIdx: startIdx + maxLen]
