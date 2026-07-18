class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        needs, haves = len(countT), 0
        length = [-1, -1]
        minLen = float("inf")
        left = 0
        window = {}

        print("COUNT T", countT)

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                haves += 1
            
            print("NEEDS", needs, "HAVES", haves)
            while needs == haves:
                if (right - left + 1) < minLen:
                    minLen = (right - left + 1)
                    length = [left, right]
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    haves -= 1
                left += 1

            print("LEFT", left, "RIGHT", right)
            
        if minLen == float("inf"):
            return ""
        
        left, right = length
        return s[left: right + 1]