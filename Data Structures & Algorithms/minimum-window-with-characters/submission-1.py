class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        window = {}
        countt = {}

        for c in t:
            countt[c] = countt.get(c, 0) + 1

        reslen = float("inf")
        res = [-1, -1]
        needs = len(countt)
        haves = 0
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countt and window[c] == countt[c]:
                haves += 1

            while needs == haves:
                if reslen > (right - left + 1):
                    reslen = (right - left + 1)
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in countt and window[s[left]] < countt[s[left]]:
                    haves -= 1

                left += 1

        if reslen == float("inf"):
            return ""

        left, right = res
        return s[left:right + 1]
