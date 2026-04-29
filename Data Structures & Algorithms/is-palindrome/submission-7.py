class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            if (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('0')):
                return True
            return False

        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not alphaNum(s[left]):
                left += 1

            while left < right and not alphaNum(s[right]):
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True





