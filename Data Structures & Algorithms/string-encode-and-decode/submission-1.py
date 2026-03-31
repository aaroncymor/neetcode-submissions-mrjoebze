class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        cur = ""
        sizes = []
        for s in strs:
            sizes.append(len(s))
            cur += s
        temp = ""
        for sz in sizes:
            temp += str(sz)
            temp += ","
        temp += "#"
        return f"{temp}{cur}"


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        sizes = []
        res = []

        while s[i] != '#':
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1

        i += 1
        for sz in sizes:
            res.append(s[i: i + sz])
            i += sz
        return res

