class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        minWin = {}
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        needs, haves = len(countT) , 0
        resLen = float("inf")
        res = []
        left = 0

        for right in range(len(s)):
            c = s[right]
            minWin[c] = minWin.get(c, 0) + 1

            if c in countT and minWin[c] == countT[c]:
                haves += 1
            
            while needs == haves:
                if (right - left + 1) < resLen:
                    resLen = (right - left + 1)
                    res = [left, right]
                
                minWin[s[left]] -= 1
                if s[left] in countT and minWin[s[left]] < countT[s[left]]:
                    haves -= 1
                left += 1
        
        if resLen == float("inf"):
            return ""

        l, r = res
        return s[l:r + 1]
