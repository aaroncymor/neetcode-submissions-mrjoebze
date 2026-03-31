class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        def isalnum(c):
            if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
                return True
            return False
    
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