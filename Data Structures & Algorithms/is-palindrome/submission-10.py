class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        s = s.lower()
        for c in s:
            if not c.isalnum():
                continue
            newStr += c
        return newStr == newStr[::-1]






