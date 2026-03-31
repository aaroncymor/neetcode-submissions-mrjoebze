class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        win = {}
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        needs, haves = len(countT), 0
        length = [-1, -1]
        minLen = float("inf")
        left = 0
        for right in range(len(s)):
            c = s[right]
            win[c] = win.get(c, 0) + 1

            if c in countT and win[c] == countT[c]:
                haves += 1

            while needs == haves:
                if minLen > (right - left) + 1:
                    minLen = (right - left) + 1
                    length = [left, right]

                win[s[left]] -= 1
                if s[left] in countT and win[s[left]] < countT[s[left]]:
                    haves -= 1

                left += 1
        if minLen == float("inf"):
            return ""
        left, right = length
        return s[left:right + 1]

