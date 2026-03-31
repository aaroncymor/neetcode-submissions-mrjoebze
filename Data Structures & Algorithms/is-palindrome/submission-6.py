class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr = ""
        for c in s:
            if not c.isalnum():
                continue
            newStr += c
        return newStr == newStr[::-1]




