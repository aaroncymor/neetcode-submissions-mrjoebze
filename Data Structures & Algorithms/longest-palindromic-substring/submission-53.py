class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxLen = 0
        resLen = [-1, -1]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                if s[i] != s[j]:
                    continue

                if j - i <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        startIdx = i
        
        return s[startIdx: startIdx + maxLen]
