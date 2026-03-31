class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        hm = {}
        for s in strs:

            # generate key
            freq = [1] * 26
            for c in s:
                idx = ord(c) - ord('a')
                freq[idx] += 1

            key = tuple(freq)
            if key not in hm:
                hm[key] = [s]
            else:
                hm[key].append(s)

        return list(hm.values())
