class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord('a') - ord(c)] += 1
            key = tuple(key)
            if key not in hm:
                hm[key] = []
            hm[key].append(s)

        return [v for k, v in hm.items()]
