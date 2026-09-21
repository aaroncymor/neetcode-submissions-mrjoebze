class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def lcs(i, j):

            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcs(i +1, j + 1)
                return memo[(i, j)]
            
            memo[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
            return memo[(i, j)]
        
        return lcs(0, 0)
                