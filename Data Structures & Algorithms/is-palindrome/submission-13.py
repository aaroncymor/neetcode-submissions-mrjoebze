class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        LETTERS = 'abcdefghijklmnopqrstuvwxyz'
        DIGITS = '0123456789'
        def isalnum(c):
            if c not in LETTERS and c not in DIGITS:
                return False
            return True
    
        while left < right:
            while left < right and not isalnum(s[left]):
                left += 1
            
            while left < right and not isalnum(s[right]):
                right -= 1

            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True