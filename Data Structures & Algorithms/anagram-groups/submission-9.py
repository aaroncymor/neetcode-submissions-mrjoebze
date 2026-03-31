class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)

            if key not in check:
                check[key] = []
            check[key].append(s)





            
        
        return [v for v in check.values()]