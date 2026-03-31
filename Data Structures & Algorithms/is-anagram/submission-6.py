class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        check = {}
        for i in range(len(s)):
            check[s[i]] = check.get(s[i], 0) + 1
            check[t[i]] = check.get(t[i], 0) - 1
        
        for v in check.values():
            if v != 0:
                return False
        return True
