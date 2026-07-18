class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(s)
        return [words for key, words in hmap.items()]
