class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for i, c in enumerate(s):
            hm[c] = hm.get(c, 0) + 1
            hm[t[i]] = hm.get(c, 0) - 1

        for key, val in hm.items():
            if val != 0:
                return False
        return True