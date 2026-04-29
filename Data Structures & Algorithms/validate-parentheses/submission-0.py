class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            c = s[i]

            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    return False
                stack.pop()

        return True if not stack else False
