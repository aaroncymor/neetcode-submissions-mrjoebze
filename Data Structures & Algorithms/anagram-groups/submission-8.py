class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in check:
                check[key] = []
            check[key].append(s)
        
        return [v for v in check.values()]