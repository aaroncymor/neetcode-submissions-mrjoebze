class Solution:
    def isAlnum(self, char):
        val = ord(char)
        print("CHAR", char, "ORD VAL", ord(char))
        if (
            (val >= ord('a') and val <= ord('z')) or
            (val >= ord('A') and val <= ord('Z')) or
            (val >= ord('0') and val <= ord('9'))
        ):
            print(f"CHAR {char} IS ALNUM")
            return True

        print(f"CHAR {char} IS NOT ALNUM")
        return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isAlnum(s[left]):
                left += 1

            while left < right and not self.isAlnum(s[right]):
                right -= 1
            
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True