class Solution:
    def isValid(self, s: str) -> bool:
        closed = { ")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in closed:
                if not stack:
                    return False
                o = stack.pop()
                if o != closed[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
