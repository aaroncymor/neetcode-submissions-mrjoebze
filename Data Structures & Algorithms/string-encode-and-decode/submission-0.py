class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += f"{len(word)}#{word}"
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        i, n = 0, 0
        while i < len(s):
            if s[i].isdigit():
                n = int(s[i])
            if s[i] == "#":
                l.append(s[i + 1:i + 1 + n])
                i = i + n + 1
                continue
            i += 1
        return l
