class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)
    
        dp = [[False] * n for _ in range(n)]
        print("DP:")
    
        for i in range(n - 1, -1, -1):
            print("I", i)
            print("J RANGE:", list(range(i, n)))
            for j in range(i, n):
                print("J", j)
                print(f"s[i]({s[i]}) == s[j]{s[j]}", s[i] == s[j])
                print(f"j - 1 <= 2? {j} - 1 < = 2?", j - 1 <= 2)
    
                # Safe boundary check for printing and logic
                inner_is_palindrome = False
                if i + 1 < n and j - 1 >= 0:
                    inner_is_palindrome = dp[i + 1][j - 1]
                    print(f"Checking dp[{i+1}][{j-1}]: {inner_is_palindrome}")
                else:
                    print(f"dp[{i+1}][{j-1}] is Out of Bounds (using default False)")
    
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
    
            print("==========================")
    
        return s[resIdx: resIdx + resLen]