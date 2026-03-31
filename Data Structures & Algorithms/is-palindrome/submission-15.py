class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alnum(c):
            v = ord(c)
            if (
                (v >= ord('a') and v <= ord('z')) or
                (v >= ord('A') and v <= ord('Z')) or
                (v >= ord('0') and v <= ord('9'))
            ):
                return True
            return False
        
        left = 0
        right = len(s) - 1

        s = s.lower()
        while left < right:
            while left < right and not is_alnum(s[left]):
                left += 1

            while left < right and not is_alnum(s[right]):
                right -= 1
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True