class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        length = [-1, -1]
        minLen = float("inf")
        left = 0
        needs, haves = len(countT), 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                haves += 1
            
            while needs == haves:
                if minLen > (right - left + 1):
                    minLen = (right - left + 1)
                    length = [left, right]
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    haves -= 1
                
                left += 1
            
        if minLen == float("inf"):
            return ""
        
        left, right = length
        return s[left:right+1]
