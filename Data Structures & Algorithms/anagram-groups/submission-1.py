class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        hm = {}
        for s in strs:

            # generate key
            key = "".join(sorted(s))
            if key not in hm:
                hm[key] = [s]
            else:
                hm[key].append(s)

        return list(hm.values())
