class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            val = ord(c)
            if (val >= ord('a') and val <= ord('z')) or (val >= ord('0') and val <= ord('9')):
                return True
            return False

        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:

            while l < r and not alphaNum(s[l]):
                l += 1

            while l < r and not alphaNum(s[r]):
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

