class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0] * 26
        for c in s:
            key = ord(c) - ord('a')
            check[key] += 1
        
        for c in t:
            key = ord(c) - ord('a')
            check[key] -= 1
        
        for v in check:
            if v != 0:
                return False
        return True