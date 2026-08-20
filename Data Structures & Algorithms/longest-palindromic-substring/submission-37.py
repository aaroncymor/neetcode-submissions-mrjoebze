class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        resIdx, resLen = 0, 0

        for i in range(N-1, -1, -1):
            for j in range(i, N):
                if s[i] != s[j]:
                    continue
                if j - i <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resLen = j - i + 1
                        resIdx = i
        
        return s[resIdx: resIdx+resLen]