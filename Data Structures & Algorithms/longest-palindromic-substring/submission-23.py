class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        N = len(s)
        dp = [[False] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):
            for j in range(i, N):

                if s[i] != s[j]:
                    continue

                if j - i <= 2 or dp[i + 1][j - 1]:
                    if resLen < j - i + 1:
                        resLen = j - i + 1
                        resIdx = i
                    dp[i][j] = True
        return s[resIdx: resIdx + resLen]