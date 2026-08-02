class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        resIdx = 0
        resLen = 0
        n = len(s)

        for i in range(n):
            l, r = i, i
            while l >= 0 and r <= n - 1:
                if s[l] != s[r]:
                    break

                if resLen < r - l + 1:
                    resLen = r - l + 1
                    resIdx = l
                
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r <= n - 1:
                if s[l] != s[r]:
                    break

                if resLen < r - l + 1:
                    resLen = r - l + 1
                    resIdx = l
                
                l -= 1
                r += 1
        
        return s[resIdx: resIdx + resLen]