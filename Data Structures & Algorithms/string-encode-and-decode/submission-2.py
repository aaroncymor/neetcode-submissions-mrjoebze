class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        return "".join(f"{len(s)}#{s}" for s in strs)



    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        i = 0
        # 5#hello5#world
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            res.append(s[i: i + length])
            i = i + length

        return res

