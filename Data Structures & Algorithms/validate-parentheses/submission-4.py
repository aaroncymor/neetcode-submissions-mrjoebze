class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in range(len(s)):
            if s[i] not in closing.keys():
                stack.append(s[i])
            else:
                opening = stack.pop()
                if opening != closing[s[i]]:
                    return False
        return True