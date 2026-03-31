class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        curr = ""
        for s in strs:
            curr += f"{len(s)},"
        curr += "#"
        for s in strs:
            curr += s
        return curr

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                break

            j = i
            while s[j] != ",":
                j += 1

            sz = int(s[i:j])
            sizes.append(sz)
            i = j + 1

        i += 1
        res = []
        for sz in sizes:
            res.append(s[i:i + sz])
            i = i + sz
        return res


