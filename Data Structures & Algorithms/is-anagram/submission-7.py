class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap = {}
        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i], 0) + 1
            hmap[t[i]] = hmap.get(t[i], 0) - 1
        
        for k, v in hmap.items():
            if v != 0:
                return False
        
        return True