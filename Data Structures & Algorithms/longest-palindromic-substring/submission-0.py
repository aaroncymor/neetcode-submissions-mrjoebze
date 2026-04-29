class Solution:
    def isPalindrome(self, s):

        def isAlNum(c):
            val = ord(c)
            if (
                (val >= ord('a') and val <= ord('z')) or
                (val >= ord('A') and val <= ord('Z')) or
                (val >= ord('0') and val <= ord('9'))
            ):
                return True
            return False

        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not isAlNum(s[left]):
                left += 1

            while left < right and not isAlNum(s[right]):
                right -= 1
            
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longestSubstr = ""
        left = 0
        for right in range(len(s)):
            while (
                (right - left) + 1 > 2 and
                not self.isPalindrome(s[left:right + 1])
            ):
                left += 1

            if(self.isPalindrome(s[left:right + 1])):
                if ((right - left) + 1) > longest:
                    longest = (right - left) + 1
                    longestSubstr = s[left:right + 1]
        return longestSubstr