class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_ctr = 0
        N = len(s)
        for i in range(N):
            l, r = i, i
            while l >= 0 and r < N:
                if s[l] != s[r]:
                    break
                palindrome_ctr += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < N:
                if s[l] != s[r]:
                    break
                palindrome_ctr += 1
                l -= 1
                r += 1
        return palindrome_ctr