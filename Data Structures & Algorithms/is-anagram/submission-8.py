class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet = [0] * 26
        for i in range(len(s)):
            key = ord(s[i]) - ord('a')
            alphabet[key] += 1
            key = ord(t[i]) - ord('a')
            alphabet[key] -= 1

        for l in alphabet:
            if l != 0:
                return False
        return True