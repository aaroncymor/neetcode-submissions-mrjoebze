class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return ""

        closing = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in range(len(s)):
            if s[i] not in closing.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False

                opening = stack.pop()
                if opening != closing[s[i]]:
                    return False
        return True