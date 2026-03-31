class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        res = [-1, -1]
        resLen = float("inf")
        left = 0
        needs = len(countT)
        haves = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                haves += 1
            
            while needs == haves:
                if resLen > (right - left + 1):
                    res = [left, right]
                    resLen = (right - left + 1)
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    haves -= 1
                left += 1
        
        if resLen == float("inf"):
            return ""
        
        left, right = res
        return s[left: right + 1]
