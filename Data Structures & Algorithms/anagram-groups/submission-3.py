class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        m = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in m:
                m[key] = [s]
            else:
                m[key].append(s)
        return list(m.values())

