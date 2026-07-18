class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(s)
        return [words for key, words in hmap.items()]
